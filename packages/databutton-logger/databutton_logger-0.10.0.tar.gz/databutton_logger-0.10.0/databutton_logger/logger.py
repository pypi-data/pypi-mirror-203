import json
import logging
import os
import re
import sys
from functools import partial
from typing import Optional

from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.context import correlation_id
from fastapi import FastAPI
from loguru import logger

from .middleware import (
    cloud_trace_context,
    http_request_context,
    http_request_middleware_func,
)

GCP_LABELS_LOG_KEY = "logging.googleapis.com/labels"
SPAN_ID_PATTERN = re.compile(r"^\w+")


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def stackdriver_sink(message, project: str):
    record = message.record
    http_request = http_request_context.get()
    labels: dict[str, str] = record.get("extra").get("labels", {})
    log_info = {
        "severity": record["level"].name,
        "message": record["message"],
        "timestamp": record["time"].timestamp(),
        "logging.googleapis.com/sourceLocation": {
            "file": record["file"].name,
            "function": record["function"],
            "line": record["line"],
        },
        GCP_LABELS_LOG_KEY: {
            "x-request-id": correlation_id.get(),
            **labels,
        },
    }
    if http_request is not None:
        log_info["httpRequest"] = http_request

    trace = cloud_trace_context.get()
    if trace is not None:
        split_header = trace.split("/", 1)

        trace_id = f"projects/{project}/traces/{split_header[0]}"

        header_suffix = split_header[1]
        span_id = SPAN_ID_PATTERN.findall(header_suffix)[0]

        log_info["logging.googleapis.com/trace"] = trace_id
        log_info["logging.googleapis.com/spanId"] = span_id
    serialized = json.dumps(log_info)
    print(serialized, file=sys.stderr)


def setup_logging_fastapi_gcp(
    app: FastAPI, *, GCP_PROJECT: Optional[str] = "databutton"
):
    app.middleware("http")(http_request_middleware_func)
    app.add_middleware(CorrelationIdMiddleware, validator=lambda str: len(str) > 10)

    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn.")
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]

    logger.remove()
    sink_for_project = partial(stackdriver_sink, project=GCP_PROJECT)
    logger.add(
        sink_for_project,
        level=os.environ.get("LOGURU_LEVEL", "INFO"),
    )

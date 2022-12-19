"""
A utility logger that allows multiple loggers to be daisy-chained.
"""
from typing import Dict, Any, Optional, IO
import sys

from spacy import Language
from .util import LoggerT


def chain_logger_v1(
    first: LoggerT,
    second: LoggerT,
    third: Optional[LoggerT] = None,
    fourth: Optional[LoggerT] = None,
    fifth: Optional[LoggerT] = None,
    sixth: Optional[LoggerT] = None,
    seventh: Optional[LoggerT] = None,
    eighth: Optional[LoggerT] = None,
    ninth: Optional[LoggerT] = None,
    tenth: Optional[LoggerT] = None,
) -> LoggerT:
    def setup_logger(nlp: Language, stdout: IO = sys.stdout, stderr: IO = sys.stderr):
        loggers = [
            first,
            second,
            third,
            fourth,
            fifth,
            sixth,
            seventh,
            eighth,
            ninth,
            tenth,
        ]
        callbacks = [
            setup(nlp, stdout, stderr) for setup in loggers if setup is not None
        ]

        def log_step(info: Optional[Dict[str, Any]]):
            nonlocal callbacks
            for log_stepper, _ in callbacks:
                log_stepper(info)

        def finalize():
            nonlocal callbacks
            for _, finalizer in callbacks:
                finalizer()

        return log_step, finalize

    return setup_logger

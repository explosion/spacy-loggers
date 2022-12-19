"""
A utility logger that looks up specific statistics and prints them to stdout.
"""
from typing import Dict, Any, Optional, IO
import sys

from spacy import Language
from .util import dict_to_dot, LoggerT


def lookup_logger_v1(substring: str) -> LoggerT:
    def setup_logger(nlp: Language, stdout: IO = sys.stdout, stderr: IO = sys.stderr):
        def log_step(info: Optional[Dict[str, Any]]):
            if info is None:
                return
            config_dot = dict_to_dot(info)
            for k, v in config_dot.items():
                if substring in k:
                    stdout.writelines([k, " -> ", str(v), "\n"])

        def finalize():
            pass

        return log_step, finalize

    return setup_logger

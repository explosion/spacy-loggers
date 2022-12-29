import pytest
import re

from spacy_loggers.util import setup_custom_stats_matcher
from .util import load_logger_from_config


valid_config_string = """
[nlp]
lang = "en"
pipeline = ["tok2vec"]

[components]

[components.tok2vec]
factory = "tok2vec"

[training]

[training.logger]
@loggers = "spacy.LookupLogger.v1"
patterns = ["^(p|P)ytorch", "zeppelin" ]
"""

invalid_config_string_empty = """
[nlp]
lang = "en"
pipeline = ["tok2vec"]

[components]

[components.tok2vec]
factory = "tok2vec"

[training]

[training.logger]
@loggers = "spacy.LookupLogger.v1"
patterns = []
"""

invalid_config_string_incorrect_pattern = """
[nlp]
lang = "en"
pipeline = ["tok2vec"]

[components]

[components.tok2vec]
factory = "tok2vec"

[training]

[training.logger]
@loggers = "spacy.LookupLogger.v1"
patterns = [")"]
"""


def test_load_from_config():
    valid_logger, nlp = load_logger_from_config(valid_config_string)
    _, _ = valid_logger(nlp)

    with pytest.raises(ValueError, match="no patterns"):
        invalid_logger, nlp = load_logger_from_config(invalid_config_string_empty)
        _, _ = invalid_logger(nlp)

    with pytest.raises(ValueError, match="couldn't be compiled"):
        invalid_logger, nlp = load_logger_from_config(
            invalid_config_string_incorrect_pattern
        )
        _, _ = invalid_logger(nlp)


def test_custom_stats_matcher():
    patterns = ["^(p|P)ytorch", "zeppelin$"]
    inputs = [
        "no match",
        "torch",
        "pYtorch",
        "pytorch",
        "Pytorch 1.13",
        "led zeppelin",
    ]
    outputs = [False, False, False, True, True, True]

    matcher = setup_custom_stats_matcher(patterns)
    assert [matcher(x) for x in inputs] == outputs

    with pytest.raises(ValueError, match="couldn't be compiled"):
        _ = setup_custom_stats_matcher([")"])

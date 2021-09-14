import pytest
from spacy import registry

FUNCTIONS = [
    ("loggers", "spacy.WandbLogger.v1"),
    ("loggers", "spacy.WandbLogger.v2"),
]


@pytest.mark.parametrize("reg_name,func_name", FUNCTIONS)
def test_registry(reg_name, func_name):
    assert registry.has(reg_name, func_name)
    assert registry.get(reg_name, func_name)

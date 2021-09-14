<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# Logging utilities for spaCy

[![PyPi Version](https://img.shields.io/pypi/v/spacy-loggers.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.python.org/pypi/spacy-loggers)

spaCy provides one logger by default, the ConsoleLogger (`spacy.ConsoleLogger.v1`).
As of version 3.2, spaCy has factored out other loggers, so that minor changes to logging
don't require a new version of spaCy. Loggers should now be provided by this package.

Currently, this package provides loggers for logging to Weights and Biases. The current logger is `spacy.WandbLogger.v2`. This package also provides `spacy.WandbLogger.v1` for backward compatibility. These loggers require installing and setting up the `wandb` package.


## Setup and installation

The package can be installed via pip:

```bash
pip install spacy-loggers
```

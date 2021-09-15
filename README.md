<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# Logging utilities for spaCy

[![PyPi Version](https://img.shields.io/pypi/v/spacy-loggers.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.python.org/pypi/spacy-loggers)

spaCy provides one logger by default, the ConsoleLogger
(`spacy.ConsoleLogger.v1`). As of version 3.2, spaCy has factored out other
loggers, so that minor changes to logging don't require a new version of spaCy.
Loggers should now be provided by this package.

Currently, this package provides loggers for logging to Weights and Biases. The
current logger is `spacy.WandbLogger.v2`. This package also provides
`spacy.WandbLogger.v1` for backward compatibility. These loggers require
installing and setting up the `wandb` package.


## Setup and installation

The package can be installed via pip:

```bash
pip install spacy-loggers
```

spacy-loggers is an extension to spaCy. It implicitly requires being able to
import spaCy. However, from the point of view of setuptools, spaCy depends on
spacy-loggers. This makes sure that spacy-loggers is installed for those who
were already relying on its functionality.


# spacy.WandbLogger.v2

## Installation

This logger requires wandb to be installed and configured:

```bash
$ pip install wandb
$ wandb login
```

## Usage

WandbLogger is a logger that sends the results of each training step to the
dashboard of the [Weights & Biases](https://www.wandb.com/) tool. To use this
logger, Weights & Biases should be installed, and you should be logged in. The
logger will send the full config file to W&B, as well as various system
information such as memory utilization, network traffic, disk IO, GPU
statistics, etc. This will also include information such as your hostname and
operating system, as well as the location of your Python executable.

**Note** that by default, the full (interpolated)
[training config](https://spacy.io/usage/training#config) is sent over to the
W&B dashboard. If you prefer to **exclude certain information** such as path
names, you can list those fields in "dot notation" in the
`remove_config_values` parameter. These fields will then be removed from the
config before uploading, but will otherwise remain in the config file stored
on your local system.

## Example config

```ini
[training.logger]
@loggers = "spacy.WandbLogger.v2"
project_name = "monitor_spacy_training"
remove_config_values = ["paths.train", "paths.dev", "corpora.train.path", "corpora.dev.path"]
log_dataset_dir = "corpus"
model_log_interval = 1000
```

| Name                   | Type            | Description                                                                                                                   |
| ---------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `project_name`         | `str`           | The name of the project in the Weights & Biases interface. The project will be created automatically if it doesn't exist yet. |
| `remove_config_values` | `List[str]`     | A list of values to include from the config before it is uploaded to W&B (default: empty).                                    |
| `model_log_interval`   | `Optional[int]` | Steps to wait between logging model checkpoints to W&B dasboard (default: None).                                              |
| `log_dataset_dir`      | `Optional[str]` | Directory containing dataset to be logged and versioned as W&B artifact (default: None).                                      |

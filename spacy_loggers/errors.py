from spacy.errors import add_codes


# fmt: off

@add_codes
class Errors:
    SPACY_LOGGERS_E880 = ("The 'wandb' library could not be found - did you "
            "install it? Alternatively, specify the 'ConsoleLogger' in the "
            "'training.logger' config section, instead of the 'WandbLogger'.")

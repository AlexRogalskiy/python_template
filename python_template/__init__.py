import logging

from .env import build_env
from .env import Default

ENV_VAR_PREFIX = "PYTHON_TEMPLATE"
ENV = build_env(
    ENV_VAR_PREFIX, {"RANGE": Default(10, validator=lambda value: type(value) is int)}
)

logging.basicConfig(
    format="\033[32m%(funcName)s\033[0m:%(lineno)s → %(msg)s", level=logging.INFO
)


def add(*args: int) -> int:
    return sum(args)


def entrypoint():
    logging.info(add(*range(ENV.range)))

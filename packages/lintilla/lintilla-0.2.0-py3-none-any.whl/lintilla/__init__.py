"""Top-level package for lintilla."""
# Core Library modules
import logging.config
from importlib.resources import as_file, files

# Third party modules
import toml  # type: ignore
import yaml  # type: ignore

__title__ = "lintilla"
__version__ = "0.2.0"
__author__ = "Stephen R A King"
__description__ = "selenium boilerplate"
__email__ = "stephen.ra.king@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2023 Stephen R A King"


LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.FileHandler
    level: DEBUG
    filename: lintilla.log
    encoding: utf-8
    formatter: timestamp

formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {name} - {message}"

loggers:
  init:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("init")

source = files("lintilla.resources").joinpath("config.toml")
with as_file(source) as _toml_path:
    _toml_text = _toml_path.read_text()
    toml_config = toml.loads(_toml_text)

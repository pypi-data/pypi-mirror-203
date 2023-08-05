"""Top Level Module."""  # noqa: RST303 D205
from _cornflakes import apply_match, eval_csv, eval_datetime, eval_type, extract_between, ini_load

from cornflakes.common import patch_module
from cornflakes.logging import attach_log, setup_logging

from cornflakes.decorator import (
    config,
    config_group,
    add_slots,
    click_cli,
    Loader,
    dataclass,
    field,
    config_field,
    Index,
)
from cornflakes.decorator.dataclass.validator import AnyUrl
from cornflakes.builder import generate_config_module
from cornflakes.parser import yaml_load


__author__ = "Semjon Geist"
__email__ = "semjon.geist@ionos.com"
__version__ = "3.2.6"  # <<COOKIETEMPLE_FORCE_BUMP>>

__all__ = [
    "click_cli",
    "ini_load",
    "eval_type",
    "eval_datetime",
    "eval_csv",
    "extract_between",
    "apply_match",
    "config",
    "config_group",
    "AnyUrl",
    "add_slots",
    "generate_config_module",
    "yaml_load",
    "attach_log",
    "setup_logging",
    "Loader",
    "dataclass",
    "field",
    "Index",
    "config_field",
    "patch_module",
]

patch_module("cornflakes")

"""
    Provides content for rc.compile_config_block() based on content under
    src/config

    (Mostly hardcoded aliases/bash helper functions)
"""

import os
import stat
from pathlib import Path

from . import package
from .lib import insert, trim_newlines


# Module methods
# ====================================================================


def get_rc_config(path):
    """provide config to be put in the rc files. Called by rc.compile_config_block()"""
    src_dir = Path(package.get_src_path())

    block = ""

    for path in ["config/default_aliases_and_functions"]:
        abs_path = src_dir.joinpath(path)
        with open(abs_path, "r") as f:
            content = f.read()
        block += insert(trim_newlines(content))

    return block


# ====================================================================

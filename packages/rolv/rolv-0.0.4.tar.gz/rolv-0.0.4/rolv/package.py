"""
    Handles getting files that are packaged into the rolv page (rolv/src/*)
"""

import os
from pathlib import Path
from functools import cache
import importlib.util


def get_version():
    with open(get_path("version"), "r") as f:
        return f.read()


def get_src_path():
    path = importlib.util.find_spec("rolv.src").submodule_search_locations[0]
    return Path(path).resolve().as_posix()


@cache
def get_path(resource):
    path = importlib.util.find_spec("rolv.src").submodule_search_locations[0]
    return Path(os.path.join(path, resource))


@cache
def get_content(resource, encoding="utf-8"):
    path = GetIncludedResourcePath(resource)
    if encoding is False:
        with open(path, "rb") as f:
            return f.read()
    else:
        with open(path, "r", encoding=encoding) as f:
            return f.read()

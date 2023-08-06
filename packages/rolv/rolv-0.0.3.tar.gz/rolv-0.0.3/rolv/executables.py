"""
    Handles copying the files under src/executables to $HOME/.local/bin.
    Also removes old files from there, and makes sure the files are available via
    an alias.
"""

import os
import stat
from pathlib import Path

from . import package


# Module methods
# ====================================================================


def get_rc_config():
    """provide config to be put in the rc files. Called by rc.compile_config_block()"""
    lines = ["# -- Executables"]
    for executable in get_executable_paths():
        name = executable.stem
        lines.append(f'alias {name}="__rolv_{name}"')

    return "\n".join(lines)


# ====================================================================


def get_executable_paths():
    src_dir = Path(package.get_src_path())
    executables_dir = src_dir.joinpath("executables")
    executables = [f for f in executables_dir.iterdir() if f.is_file()]
    return executables


def sync_executables():
    bin_path = Path(os.getenv("HOME") + "/.local/bin").resolve()

    # remove existing execs starting with __rolv_
    for path in bin_path.iterdir():
        if path.name.startswith("__rolv_"):
            print(f"removing: {path.as_posix()}")
            os.remove(path)

    # place / overwrite executables
    for executable in get_executable_paths():
        if executable.name == "readme.md":
            continue

        with open(executable, "r") as f:
            content = f.read()

        dst = bin_path.joinpath(f"__rolv_{executable.name}")
        print(f"writing: {dst.as_posix()} (src: {executable.as_posix()})")

        with open(dst, "w") as f:
            f.write(content)

        make_executable(dst)


def make_executable(path):
    """Basically 'chmod +x path', but only for current user"""
    os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC)

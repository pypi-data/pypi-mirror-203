"""
    This file handles all the interactions with the rc files (bashrc, zshrc, etc)
    It does not determine the config to be added itself, for that it calls get_rc_config() methods of other modules.
"""

import os
import re
from pathlib import Path

from . import executables, config
from .lib import insert, trim_trailing_newlines


def compose_config():
    """Called to compose new config to be put in the bashrc. Lacks the fencing, just the config.
    If you want to read the current config block, see get_config_block()"""

    block = ""
    block += config.get_rc_config()
    block += executables.get_rc_config()

    return block


def get_rc_file_paths():
    """Finds rc file paths if they exist in the default location, unless ROLV_RC_FILE_PATH is set, then it will only return that value."""
    # use single, configured path
    explicit_path = os.getenv("ROLV_RC_FILE_PATH")
    if explicit_path is not None:
        explicit_path = Path(explicit_path).resolve()
        if explicit_path.exists() == False:
            print(f'Provided path ROLV_RC_FILE_PATH="{explicit_path.as_posix()}" does not exist. Get your shit together lmao. Aborting.')
            exit(1)
        return [Path(explicit_path).resolve()]

    # update all rc paths that are found
    res = []
    for path in [".zshrc", ".bashrc"]:
        abs_path = Path(os.getenv("HOME") + "/" + path).resolve()
        if abs_path.exists():
            res.append(abs_path)
    return res


def set_rc_files():
    """Adds/updates the config block to rc file paths."""
    for abs_path in get_rc_file_paths():
        set_rc_file(abs_path)


def set_rc_file(path):
    """Updates/Places the rolv config block in the given rc file"""
    if path.exists() is False:
        print(f"File {path.as_posix()} not found. Aborting.")
        exit(0)

    rolv_block, other = get_config_block(path)
    if rolv_block:
        print(f"Rolv config block exists in {path.as_posix()} file - overwriting")
    else:
        print(f"Adding 'rolv config' block to {path.as_posix()}")

    contents = other

    # do nice spacing
    lines = [x.strip() for x in contents.split("\n")]
    if contents[-1] != "":
        contents += "\n"

    contents += "\n# <rolv config>\n# =======================================================\n"
    contents += insert(compose_config(), space=0)
    contents += "# =======================================================\n# </rolv config>\n"

    with open(path, "w") as f:
        f.write(contents)


def remove_bashrc_block(path):
    block, other = get_config_block(path)
    with open(path, "w") as f:
        f.write(other)


def get_config_block(path, match_preceding_newlines=True):
    """Will return .bashrc content split into the rolv config block and all the other contents. To overwrite block, just use other content and add block to it"""

    with open(path, "r") as f:
        contents = f.read()

    in_block = False
    re_begin = re.compile(r"^ *# *<rolv config> *")
    re_end = re.compile(r"^ *# *</rolv config> *")

    other_lines = []
    block_lines = []
    for line in contents.split("\n"):
        # enter block
        if in_block == False:
            if re_begin.match(line):
                in_block = True

                # match single header empty newline with the matched block
                if match_preceding_newlines:
                    while len(other_lines) > 0 and other_lines[-1].strip() == "":
                        block_lines.append(other_lines.pop())

        # write all other lines to either block or "other" output
        if in_block:
            block_lines.append(line)
        else:
            other_lines.append(line)

        # exit block
        if in_block:
            if re_end.match(line):
                in_block = False

    # trim newlines at the end of the file
    other_lines = trim_trailing_newlines(other_lines)

    return "\n".join(block_lines), "\n".join(other_lines)

import os
import re
from pathlib import Path

def set_bashrc():
    # config_path = Path(os.getenv("HOME") + '/.rolv').resolve()
    # script_path = Path(os.getenv("HOME") + '/.local/bin').resolve()
    # print(config_path, script_path, bashrc_path)

    bashrc_path = Path(os.getenv("HOME") + '/.bashrc').resolve()
    if bashrc_path.exists() is False:
        print(f'File {bashrc_path.as_posix()} not found. Aborting.')
        exit(0)

    rolv_block, other = get_bashrc_block()
    if rolv_block:
        print(f"Rolv config block exists in {bashrc_path.as_posix()} file - overwriting")
    else:
        print(f"Adding 'rolv config' block to {bashrc_path.as_posix()}")

    contents = other

    # do nice spacing
    lines = [x.strip() for x in contents.split("\n")]
    if contents[-1] != '':
        contents += "\n"
    
    contents += "\n# <rolv config>\n# =======================================================\n"
    contents += "# =======================================================\n# </rolv config>\n"

    with open(bashrc_path, 'w') as f:
        f.write(contents)

def remove_bashrc_block():
    bashrc_path = Path(os.getenv("HOME") + '/.bashrc').resolve()
    block, other = get_bashrc_block()
    with open(bashrc_path, 'w') as f:
        f.write(other)
    
    
def get_bashrc_block(match_preceding_newlines=True, trim_trailing_newlines=True):
    """ Will return .bashrc content split into the rolv config block and all the other contents. To overwrite block, just use other content and add block to it"""
    bashrc_path = Path(os.getenv("HOME") + '/.bashrc').resolve()
    with open(bashrc_path, 'r') as f:
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
                    while len(other_lines) > 0 and other_lines[-1].strip() == '':
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
    while len(other_lines) > 0 and other_lines[-1].strip() == '':
        other_lines.pop()

    return "\n".join(block_lines), "\n".join(other_lines)


"""
    General helper functions
"""


def insert(text, space=1):
    """Tests if last char is newline, and if not, will add the newline"""
    # make sure that the text at least ends on a new line
    if len(text) == 0 or text[-1] != "\n":
        text = text + "\n"

    # add extra spacing between blocks
    text += "\n" * space

    return text


def trim_trailing_newlines(text_or_lines):
    # make sure that we have lines as input
    if isinstance(text_or_lines, str):
        input_is_lines = False
        lines = text_or_lines.split("\n")
    else:
        input_is_lines = True
        lines = text_or_lines

    # remove trailing newlines
    while len(lines) > 0 and lines[-1].strip() == "":
        lines.pop()

    # return in some format as received
    if input_is_lines:
        return lines
    return "\n".join(lines)


def trim_preceeding_newlines(text_or_lines):
    # make sure that we have lines as input
    if isinstance(text_or_lines, str):
        input_is_lines = False
        lines = text_or_lines.split("\n")
    else:
        input_is_lines = True
        lines = text_or_lines

    # remove trailing newlines
    while len(lines) > 0 and lines[0].strip() == "":
        lines.pop(0)

    # return in some format as received
    if input_is_lines:
        return lines
    return "\n".join(lines)


def trim_newlines(text_or_lines):
    text_or_lines = trim_preceeding_newlines(text_or_lines)
    text_or_lines = trim_trailing_newlines(text_or_lines)
    return text_or_lines

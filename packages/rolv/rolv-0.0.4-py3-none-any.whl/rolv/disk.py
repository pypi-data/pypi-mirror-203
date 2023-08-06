""" Handles creating folders, removing folders, etc """

import os
import shutil
from pathlib import Path


def ensure_rolv_folder_exists():
    path = Path(os.getenv("HOME") + "/.rolv").resolve()
    path.mkdir(exist_ok=True)


def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        print(f"removing folder: {path.as_posix()}")
        os.unlink(path)
    else:
        print(f"removing folder: {path.as_posix()}")
        shutil.rmtree(path)

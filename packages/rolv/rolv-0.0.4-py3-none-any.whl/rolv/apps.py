""" Installation of multi-file applications, as stored under src/apps """
import os
import shutil

from pathlib import Path

from .lib import insert
from . import package, disk

# Module methods
# ====================================================================


def get_rc_config(path):
    """provide config to be put in the rc files. Called by rc.compile_config_block()"""
    text = "# -- Apps\n"
    text += insert(get_fzf_rc_config(path))

    return text


# App: FZF
# ====================================================================


def get_fzf_rc_config(path):
    text = ""
    if "bash" in path.name:
        text = "# fzf\nsource ~/.rolv/fzf/.fzf.bash"
    if "zsh" in path.name:
        text = "# fzf\nsource ~/.rolv/fzf/.fzf.zsh"
    return text


def get_fzf_dst_path():
    return Path(os.getenv("HOME") + "/.rolv/fzf").resolve()


def install_fzf():
    disk.ensure_rolv_folder_exists()

    src_path = Path(package.get_src_path()).joinpath("apps/fzf")
    dst_path = get_fzf_dst_path()

    print(f"writing: {dst_path.as_posix()} (src: {src_path.as_posix()})")
    shutil.copytree(src_path, dst_path)


def uninstall_fzf():
    disk.rm_r(get_fzf_dst_path())


def sync_apps():
    uninstall_fzf()
    install_fzf()

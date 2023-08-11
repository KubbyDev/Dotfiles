import argparse
import sys
from Windows.update_windows import WindowsPlatform
from Linux.update_linux import LinuxPlatform
import os
from pathlib import Path

import utils
from utils import Aliases


platform: utils.Platform


def get_aliases() -> Aliases:
    res = {}
    # gets aliases from yamls
    # Gets aliases for custom commands
    files = os.path.listdir(Path('Commands/Impl'))
    files.remove('utils.py')
    commands = [file[:-3] for file in files]
    res += {cmd: f"python {Path(platform.get().dotfiles_dir()) / Path('Commands/mux.py')} {cmd}" for cmd in commands}


def install():
    pass


def update():
    aliases = get_aliases()
    platform.update_aliases(aliases)


if __name__ == "__main__":
    global platform
    if sys.platform == 'win32':
        platform = WindowsPlatform()
    elif sys.platform == 'linux':
        platform = LinuxPlatform()
    else:
        raise RuntimeError(f"Platform {sys.platform} not supported")
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", store=True)
    args = parser.parse_args()
    if args.install:
        install()
    update()

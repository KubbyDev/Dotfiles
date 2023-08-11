from Commands.utils import *


def main(message):
    if cmd_output("git diff --name-only --cached") != "":
        if get_consent("Detected staged files. Redo add anyways ?"):
            cmd_ret("git reset HEAD .")
            cmd_ret("git add .")
    else:
        cmd_ret("git add .")
    cmd_ret("git status")
    if not get_consent("Commit ?"):
        return
    if not cmd_ret(f'git commit -m "{message}"'):
        return
    cmd_ret("git push")


def check_args():
    pass

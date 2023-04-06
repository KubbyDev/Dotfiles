import os
import subprocess
import sys


# Executes the command and returns its exit code
def cmd_ret(cmd, silent=False):
    file = subprocess.DEVNULL if silent else None
    return subprocess.call(cmd, shell=True, stdout=file, stderr=file)


# Executes the command and returns its output. Silent
def cmd_output(cmd):
    return os.popen(cmd).read()


def get_consent(msg):
    print(msg + " [Y/N] ", end='')
    res = input()
    return res == "" or res.lower() in ["yes", "y"]


def commit_main(message, tag):
    if cmd_output("git diff --name-only --cached").strip() != "":
        if get_consent("Detected staged files. Redo add anyways ?"):
            cmd_ret("git reset HEAD .")
            cmd_ret("git add .")
    else:
        cmd_ret("git add .")
    cmd_ret("git status")
    if not get_consent("Commit ?"):
        return
    if cmd_ret(f'git commit -m "{message}"') != 0:
        return
    if tag is not None:
        i = 0
        while cmd_ret(f'git tag -a "{tag}-{i}" -m "{message}"', silent=True) != 0:
            i += 1
    cmd_ret("git push --follow-tags")


def pushforce_main():
    cmd_ret("git fetch")
    branchname = cmd_output("git branch --show-current").strip()
    if cmd_output(f"git diff --name-only origin/{branchname} HEAD").strip() != "":
        print("Diff detected between remote branch and local HEAD")
        cmd_ret(f"git diff origin/{branchname} HEAD")
        if not get_consent("Push force ?"):
            return
    cmd_ret("git push --force-with-lease")


def main(arguments):
    selection = arguments[0]
    if selection == 'commit':
        if len(arguments) < 2 or len(arguments) > 3:
            print("Usage: commit <message> [tag]")
            return
        commit_main(arguments[1], arguments[2] if len(arguments) > 2 else None)
    elif selection == 'pushforce':
        if len(arguments) > 1:
            print("Usage: pushforce")
            return
        pushforce_main()
    else:
        raise ValueError()


if __name__ == '__main__':
    main(sys.argv[1:])

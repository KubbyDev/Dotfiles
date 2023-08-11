from Commands.utils import *


def pushforce_main():
    cmd_ret("git fetch")
    branchname = cmd_output("git branch --show-current")
    if cmd_output(f"git diff --name-only origin/{branchname} HEAD") != "":
        print("Diff detected between remote branch and local HEAD")
        cmd_ret(f"git diff origin/{branchname} HEAD")
        if not get_consent("Push force ?"):
            return
    cmd_ret("git push --force-with-lease")

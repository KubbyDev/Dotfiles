import os
import subprocess


def cmd_ret(cmd: str, silent: bool=False) -> bool:
    """
    Executes the command and returns True if it succeeded, False if it failed
    The command output will be printed on the terminal unless silent is True
    """
    fd = subprocess.DEVNULL if silent else None
    return subprocess.call(cmd, shell=True, stdout=fd, stderr=fd) == 0


def cmd_output(cmd: str) -> str:
    """
    Executes the command and returns its output stripped
    Nothing is printed on the terminal
    """
    return os.popen(cmd).read().strip()


def get_consent(msg: str) -> bool:
    """
    Displays a message and waits for the user to give consent or not
    """
    print(msg + " [Y/N] ", end='')
    res = input()
    return res == "" or res.lower() in ["yes", "y"]

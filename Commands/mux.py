import importlib
import os
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List
import Impl


class Command:

    def main(self):
        pass

    def add_args(self, parser: ArgumentParser):
        """"""
        pass

    def get_args(self, ):


def run_command():
    parser = ArgumentParser()
    for cmd in os.listdir(Path(__file__) / Path('Impl')):
        importlib.import_module(cmd)
    parser.parse_args(args=sys.argv[2:])

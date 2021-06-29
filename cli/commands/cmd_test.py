"""CLI file to start tests"""

from os import path
from subprocess import run

import click


@click.command()
@click.argument("tests_path", default=path.join("snake_eyes", "tests"))
def cli(tests_path: str):
    """Run the tests"""
    cmd = "pytest %s" % tests_path
    return run(cmd, shell=True)

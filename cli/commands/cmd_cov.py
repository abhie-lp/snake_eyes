"""CLI file for code coverage"""

from subprocess import run
import click


@click.command()
@click.argument("path", default="snake_eyes")
def cli(path: str):
    """Run a test coverage report"""
    cmd = "pytest --cov-report term-missing --cov %s" % path
    return run(cmd, shell=True)

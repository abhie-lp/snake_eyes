"""CLI file to run flake8 command"""

from subprocess import run
import click


@click.command()
@click.option("--skip-init/--no-skip-init", default=True,
              help="Skip __init__.py files")
@click.argument("path", default="snake_eyes")
def cli(skip_init: bool, path: str):
    """Run the flake8 over project"""
    exclude = ""

    if skip_init:
        exclude = "--exclude __init__.py"

    cmd = "flake8 %s %s" % (path, exclude)
    return run(cmd, shell=True)

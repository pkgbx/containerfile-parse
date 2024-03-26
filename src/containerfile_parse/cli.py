import json
import pathlib

import click

from . import containerfile


@click.group
def cli(): pass


@cli.command
def version():
    """
    Shows the program version.
    """
    click.echo('v0.1.0')


@cli.command
@click.argument('path', type=click.Path(path_type=pathlib.Path))
@click.option('-p', '--pretty', is_flag=True, help='prints formatted json if used')
def inspect(path: pathlib.Path, pretty):
    """
    Inspect a containerfile in PATH.
    """
    parser = containerfile.from_filepath(path)

    click.echo(containerfile.as_json(parser, pretty=pretty))

def run():
    cli()


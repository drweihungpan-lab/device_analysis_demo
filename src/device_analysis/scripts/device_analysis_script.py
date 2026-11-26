"""CLI script for the device_analysis package. This will be called on the command line"""

import click

from device_analysis.device_analysis import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def device_analysis_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))

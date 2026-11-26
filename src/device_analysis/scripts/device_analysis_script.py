"""Command-line entry point for the device_analysis package."""

from pathlib import Path

import click

from device_analysis.device_analysis import (
    format_summaries,
    read_counts,
    summarize_devices,
)


@click.command()
@click.argument(
    "input_file", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.option(
    "-o",
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    default=Path("device_summary.txt"),
    show_default=True,
    help="Path of the text file to write.",
)
@click.version_option()
def device_analysis_cli(input_file, output):
    """Summarize daily cycle counts per device from INPUT_FILE (CSV).

    Writes device name, number of non-zero days, median and mean cycle.
    """
    try:
        summaries = summarize_devices(read_counts(input_file))
    except ValueError as error:
        raise click.ClickException(str(error)) from error
    output.write_text(format_summaries(summaries), encoding="utf-8")
    click.echo(f"Wrote {len(summaries)} device summaries to {output}")

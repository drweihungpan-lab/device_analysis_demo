"""Summarize daily device cycle counts per device."""

import csv
import statistics
from dataclasses import dataclass
from pathlib import Path

from .logger_config import logger

REQUIRED_COLUMNS = ("device_id", "daily_count")
HEADER = ("device", "nonzero_days", "median_cycle", "mean_cycle")


@dataclass(frozen=True)
class DeviceSummary:
    """Per-device statistics of the daily cycle count."""

    device: str
    nonzero_days: int
    median_cycle: float
    mean_cycle: float


def read_counts(path):
    """Read a CSV with `device_id` and `daily_count` columns.

    Returns {device_id: [daily_count, ...]} in file order.
    """
    counts = {}
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"{path} is missing column(s): {', '.join(missing)}")
        for row in reader:
            counts.setdefault(row["device_id"], []).append(int(row["daily_count"]))
    logger.debug("Read %d device(s) from %s", len(counts), path)
    return counts


def summarize_devices(counts):
    """Return one DeviceSummary per device, sorted by device name.

    Median and mean are taken over all days, including zero-count days.
    """
    return [
        DeviceSummary(
            device=device,
            nonzero_days=sum(1 for value in values if value != 0),
            median_cycle=float(statistics.median(values)),
            mean_cycle=float(statistics.mean(values)),
        )
        for device, values in sorted(counts.items())
        if values
    ]


def format_summaries(summaries):
    """Render summaries as tab-separated text with a header line."""
    lines = ["\t".join(HEADER)]
    lines += [
        f"{s.device}\t{s.nonzero_days}\t{s.median_cycle:.2f}\t{s.mean_cycle:.2f}"
        for s in summaries
    ]
    return "\n".join(lines) + "\n"


def format_table(summaries):
    """Render summaries as an aligned table for display on screen."""
    rows = [HEADER] + [
        (s.device, str(s.nonzero_days), f"{s.median_cycle:.2f}", f"{s.mean_cycle:.2f}")
        for s in summaries
    ]
    widths = [max(len(row[i]) for row in rows) for i in range(len(HEADER))]

    def render(row):
        first = row[0].ljust(widths[0])
        rest = [cell.rjust(width) for cell, width in zip(row[1:], widths[1:])]
        return "  ".join([first, *rest])

    separator = "  ".join("-" * width for width in widths)
    return "\n".join([render(rows[0]), separator, *map(render, rows[1:])])

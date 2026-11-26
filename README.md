# device_analysis package

This is a package called device_analysis. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Usage

Summarize daily cycle counts per device from a CSV with `device_id`, `date`
and `daily_count` columns (example data copied from `3R-device-example` is in
`data/device_counts.csv`):

```bash
pip install -e .
device_analysis data/device_counts.csv -o device_summary.txt
```

The output is a tab-separated text file with one row per device:

```
device	nonzero_days	median_cycle	mean_cycle
DEV-A	352	179.00	174.00
DEV-B	351	217.00	209.94
DEV-C	357	260.00	254.77
```

Median and mean are computed over all days, including zero-count
(maintenance) days.

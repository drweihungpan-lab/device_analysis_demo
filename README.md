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

The results are shown on the screen:

```
$ device_analysis data/device_counts.csv -o device_summary.txt
device  nonzero_days  median_cycle  mean_cycle
------  ------------  ------------  ----------
DEV-A            352        179.00      174.00
DEV-B            351        217.00      209.94
DEV-C            357        260.00      254.77

Wrote 3 device summaries to device_summary.txt
```

They are also saved to a tab-separated text file (`device_summary.txt`), with
one row per device:

```
device	nonzero_days	median_cycle	mean_cycle
DEV-A	352	179.00	174.00
DEV-B	351	217.00	209.94
DEV-C	357	260.00	254.77
```

Median and mean are computed over all days, including zero-count
(maintenance) days.

### Second example dataset

`data/device_counts_example2.csv` is a smaller synthetic dataset (seed
`20260101`): three devices (`DEV-X`, `DEV-Y`, `DEV-Z`) over 30 days
(2026-01-01 to 2026-01-30), with about 15% zero-count days.

```
$ device_analysis data/device_counts_example2.csv -o example2_summary.txt
device  nonzero_days  median_cycle  mean_cycle
------  ------------  ------------  ----------
DEV-X             26         51.50       45.17
DEV-Y             24        113.00       94.37
DEV-Z             28        304.50      291.93

Wrote 3 device summaries to example2_summary.txt
```

With more zero days, the mean drops clearly below the median.

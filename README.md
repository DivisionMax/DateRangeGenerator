# Date Range Generator

_Developed with Python 3.6.4_

By default generates date ranges six months apart

```
usage: date_range_generator.py [-h] [--period PERIOD]
                               [--period_type {weeks,months,days}]
                               [--start START_DATE] [--end END_DATE]

Generate ranges of date from a given date, to a target date

optional arguments:
  -h, --help            show this help message and exit
  --period PERIOD       The distance between generated periods
  --period_type {weeks,months,days}
                        The type of period to use when generating ranges
  --start START_DATE    The type of period to start generating date ranges
                        from. Format: "2015-02-31"
  --end END_DATE        The type of period to generate date ranges until.
                        Format: "2015-02-31"
```

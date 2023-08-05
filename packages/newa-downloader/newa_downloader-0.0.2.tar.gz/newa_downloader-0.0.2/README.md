# NEWA Downloader

This is a small package to download data from the new european wind atlas.
It is by no means complete or very robust, but should do its job.

## Installation

Install via 
``pip install NEWA_downloader`` or 
```
git clone https://github.com/Hkorb/newa_downloader
cd newa_downloader && pip install .
```


## Usage


```python 
time_span = TimeSpan(datetime(2008, 1, 1), datetime(2008,1,2))
point = DataPoint(57.18, 18.3)
file = Path("visby_2008.nc")
variables = ["WS"]
heights = [50, 100]
download_mesoscale_timeseries(file, variables, point, time_span, heights)
```


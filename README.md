# Owners-Geo
> Geocode owner addresses and write them to a GeoJSON FeatureCollection

## Setup

#### Install Dependencies

This script requires the `geocoder` and `psycopg2` libraries - install them by running:

```bash
pip3 install -r requirements.txt
```

#### Additional Requirements

You'll need to include a `credentials.py` file in the root directory with the appropriate Postgres database credentials, formatted like so:

```python
user = 'user'
password = 'password'
dbname = 'dbname'
host = 'host'

```

## Use

Run the script with the command

```bash
python3 run.py
```

As the script geocodes each owner address, it'll add the data to a FeatureCollection, which will ultimately be written to a file named `-owners.geojson`, prefixed with the date. The data in this file can be used for any number of mappy things.

## Reference

https://developers.google.com/maps/documentation/javascript/geocoding

https://github.com/DenisCarriere/geocoder

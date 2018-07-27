# Format the list of GeoJSON data and write it to a file.
import datetime

def write(filename, geojson):
    file = open(filename, 'w+')
    file.write(geojson)

def execute(geojson):
    filename = f'{datetime.datetime.today().strftime("%Y-%m-%d")}-owners.geojson'
    print(f'Writing to file {filename}')
    write(filename, geojson)

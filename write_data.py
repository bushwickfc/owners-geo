# Format the list of GeoJSON data and write it to a file.

def write(filename, geojson):
    file = open(filename, 'w+')
    file.write(geojson)

def execute(geojson):
    filename = 'owners.geojson'
    print(f'Writing to file {filename}')
    write(filename, geojson)

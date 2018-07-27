# Geocode the list of addresses and return a list of geoJSON data.
import geocoder
import time
import json

# Piece the query results together into a cohesive address string.
def prepare_data(od):
    return ', '.join(od)

# Hit Google's geocoder API.
def handle_geocode(address):
    return geocoder.google(address)

# Geocode each address and format it as a geoJSON.
# The Google geocoder is rate limited, so retry those until you get a response.
# See 'Status Codes' at https://developers.google.com/maps/documentation/javascript/geocoding
def geocode(stringified_data):
    geojson = {'type': 'FeatureCollection', 'features': []}
    for address in stringified_data:
        cont = False
        while not cont:
            geo_data = handle_geocode(address)
            if geo_data.status == 'OK':
                print(f'Success: geocoded {address}')
                geojson['features'].append(geo_data.geojson['features'][0])
                cont = True
            elif geo_data.status == 'OVER_QUERY_LIMIT':
                print(f'Over query rate limit: could not geocode {address} - retrying in 2 seconds.')
                time.sleep(2)
            else:
                print(f'Error: unable to geocode {address} - {geo_data.status}')
                # If it fails to geocode, just continue to the next iteration.
                # TODO: Maybe get back a list of failed addresses, too?
                cont = True

    return json.dumps(geojson)

def execute(owner_data):
    print('Geocoding owner address data. This may take a few minutes...')
    stringified_data = [prepare_data(od) for od in owner_data]
    return geocode(stringified_data)

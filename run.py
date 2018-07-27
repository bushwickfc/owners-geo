import fetch_data
import geocode
import write_data

def execute():
    owner_data = fetch_data.execute()
    geojson = geocode.execute(owner_data)
    write_data.execute(geojson)
    print('Done!')

if __name__ == '__main__':
    execute()

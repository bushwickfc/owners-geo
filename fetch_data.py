# Fetch the owner data.
import psycopg2
import credentials # This file is gitignored - you'll need to provide your own copy

def fetch_data(conn):
    query = 'SELECT address, city, state, zipcode FROM owner'
    with conn.cursor() as cursor:
        cursor.execute(query)
        owner_data = cursor.fetchall()

    return owner_data


def execute():
    print('Fetching owner address data...')
    conn = psycopg2.connect(f'''host={credentials.host}
                                user={credentials.user}
                                password={credentials.password}
                                dbname={credentials.dbname}''')

    return fetch_data(conn)

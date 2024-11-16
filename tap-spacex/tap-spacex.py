import singer
import pandas as pd

LOGGER = singer.get_logger()

schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'date_utc': {'type': 'string', 'format': 'date-time'},
    }
}

def main():
    import numpy as np
    
    url = 'https://api.spacexdata.com/v4/launches'
    df = pd.read_json(url)
    
    # Select and clean only the columns we want according to our schema
    df_cleaned = df[['id', 'name', 'date_utc']].copy()
    
    # Convert to records
    records = df_cleaned.to_dict(orient='records')
    
    # Write schema and records
    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', records)

if __name__ == '__main__':
    main()
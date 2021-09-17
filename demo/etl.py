import configparser
from utils import extract_data, load_data

# get configuration parameters
config = configparser.ConfigParser()
config.read('params.ini')
start_date = config['CONFIG']['startDate']
end_date = config['CONFIG']['endDate']
dest_db = config['CONFIG']['database']

# etl function as entry point
def demo_etl():
    df = extract_data(start_date, end_date)
    load_data(df, dest_db)



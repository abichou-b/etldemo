import sqlite3
from datetime import datetime
import pandas as pd
import requests


def extract_data(start_date, end_date):
    r = requests.get('https://hubeau.eaufrance.fr/api/v1/qualite_nappes/analyses' \
                      '?&date_debut_prelevement={' \
                      'debut}&date_fin_prelevement={fin}'.format(debut=start_date,
                                                                        fin=end_date))
    analyses = r.json()
    data_dict = {
        'station' : [],
        'result': [],
        'date' : [],
        'qualification' : []
        }
    for rec in analyses['data']:
        data_dict['station'].append(rec['bss_id'])
        data_dict['result'].append(rec['resultat'])
        data_dict['date'].append(datetime.strptime(rec['date_debut_prelevement'],'%Y-%m-%d'))
        data_dict['qualification'].append(rec['nom_qualification'])
    data_df = pd.DataFrame(data_dict)
    return data_df

def load_data(data_df, dest_db):
    conn = sqlite3.connect('quality_station.db')
    cursor = conn.cursor()
    sql_query = """
        CREATE TABLE IF NOT EXISTS quality(
           station VARCHAR(20),
           result float(6),
           qualification VARCHAR(20),
           date datetime
        )
        """
    cursor.execute(sql_query)
    conn.commit()
    data_df.to_sql('quality', conn, index=False, if_exists='append')
    conn.close()
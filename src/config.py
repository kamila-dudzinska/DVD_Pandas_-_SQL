"""
Created on Mon Mar 23 19:27:31 2026

@author: Kamila Dudzińska
"""

#import modułów
import os
from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from sql_query import sql_filmy
from dotenv import load_dotenv

#odczyt pliku .env
#modyfikacja scieżki
env_path = Path(__file__).parent/'.env'
load_dotenv(dotenv_path=env_path)


print(os.getenv('DB_HOST'))
print(os.getcwd())


# pobueranie danych z systemu - zmienne srodowiskowe
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

#tworzenie url_połączenia
url_conn1 = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# data loader -funkcja i silnik
def load_data():
    engine = create_engine(url_conn1)
    df = pd.read_sql(sql_filmy, engine)
    return df

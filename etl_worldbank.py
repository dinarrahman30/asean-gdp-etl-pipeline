import requests
import pandas as pd
from sqlalchemy import create_engine
from prefect import task, flow
from dotenv import load_dotenv
import os

load_dotenv()

@task(retries=3, retry_delay_seconds=5)
def extract_data():
    url = "http://api.worldbank.org/v2/country/IDN;MYS;THA;SGP;VNM/indicator/NY.GDP.MKTP.CD?format=json&per_page=1000"
    response = requests.get(url)
    data = response.json()[1]
    return data

@task
def transform_data(data):
    df = pd.DataFrame(data)
    df['country'] = df['country'].apply(lambda x: x['value'])
    df = df[['country', 'value', 'date']]
    df.columns = ['country', 'gdp', 'year']
    
    df = df.dropna()

    df['year'] = pd.to_numeric(df['year'])
    df['gdp'] = pd.to_numeric(df['gdp'])

    return df

@task
def load_data(df):
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "worldbank_db")
    
    # Merakit string koneksi
    connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    engine = create_engine(connection_string)
    df.to_sql('gdp_data', engine, if_exists='replace', index=False)
    print("Data berhasil dimuat ke database!")

@flow
def worldbank_etl():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

if __name__ == "__main__":
    worldbank_etl()
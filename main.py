import os
from webscraping import Scrapper
from sqlalchemy import create_engine

# Crio conexão banco de dados Postgres
engine = create_engine(
    "postgresql+psycopg2://{}:{}@{}/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_ADDRESS"),
        os.environ.get("POSTGRES_DATABASE"),
    )
)
connection = engine.connect()

scrap = Scrapper()
df = scrap.scrapping_pokemon()
df.to_sql("pokemonstats", connection, if_exists="append", index=False)

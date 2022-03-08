from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utiles import database_exists,create_database
from local_settings import postgresql as settings
postgres = ('pguser':'ankit',
            'pgpasswd':'@nkit2073'
            'pghost':'localhost'
            'pgport':'5432'
            'pgdb':'ankit'
            )
def get_engine(ankit,@nkit2073,localhost,5432,postgres):
    url = f"POSTGRESQL"

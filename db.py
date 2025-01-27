from config import DB_CREDENTIALS
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Create a connection to the database
DB_USERNAME = DB_CREDENTIALS['DB_USERNAME']
DB_PASSWORD = DB_CREDENTIALS['DB_PASSWORD']
DB_NAME = DB_CREDENTIALS['DB_NAME']
DB_HOST = DB_CREDENTIALS['DB_HOST']
DB_PORT = DB_CREDENTIALS['DB_PORT']

connection_string = (
    'mariadb+mariadbconnector://'
    f'{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
engine = create_engine(
    connection_string,
    pool_recycle=3600,
    pool_size=1,
    pool_pre_ping=True,
    connect_args={'ssl': False}
)

Base = declarative_base()
Base.metadata.bind = engine
Session = scoped_session(sessionmaker(bind=engine))

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlUrl = 'mysql+pymysql://root:teste12@127.0.0.1:8000/list_todo'
engine = create_engine(sqlUrl)
session = sessionmaker(autoflush=False, bind=engine)
base = declarative_base()

def connection():
    currentSession = session()

    try:
        yield currentSession
    except:
        currentSession.close()
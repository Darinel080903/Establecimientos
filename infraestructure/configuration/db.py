from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

connection = os.getenv('URR')
user = os.getenv('USS')
password = os.getenv('PSS')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{connection}:3306/establishment', pool_size=10, max_overflow=20, pool_recycle=60)
meta = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()

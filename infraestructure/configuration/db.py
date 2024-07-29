from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

connection = os.getenv('URR2')
user = os.getenv('USS2')
password = os.getenv('PSS2')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{connection}:3306/establishment', pool_size=10, max_overflow=20, pool_recycle=60)
meta = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()

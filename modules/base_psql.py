from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://percona:12345@localhost:5432/company")
Session = sessionmaker(bind=engine)

Base = declarative_base()
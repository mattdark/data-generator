from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://user:password@localhost/company")
#engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/company")
Session = sessionmaker(bind=engine)
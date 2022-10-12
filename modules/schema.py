from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

from .base_mysql import Base
#from .base_psql import Base

class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    job = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    city = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)

    def __init__(self, first_name, last_name, job, address, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.address = address
        self.city = city
        self.email = email
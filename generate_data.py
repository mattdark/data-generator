from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
from sqlalchemy.orm import scoped_session

from faker import Faker
import pandas as pd
import numpy as np
from tqdm import tqdm

from modules.schema import Employee
from modules.base_mysql import Session, engine, Base
#from modules.base_psql import Session, engine, Base

fake = Faker()

def create_dataframe(x):
    data = pd.DataFrame()
    for i in tqdm(range(x), desc='Creating DataFrame'):
        data.loc[i, 'first_name'] = fake.first_name()
        data.loc[i, 'last_name'] = fake.last_name()
        data.loc[i, 'job'] = fake.job()
        data.loc[i, 'address'] = fake.address()
        data.loc[i, 'city'] = fake.city()
        data.loc[i, 'email'] = fake.email()
    return data
      
def load_data(data):
    session = Session()
    for row in tqdm(data.itertuples(), desc='Loading Data'):
        e = Employee(row.first_name, row.last_name, row.job, row.address, row.city, row.email)
        session.add(e)
        session.commit()

def thread_worker(data):
    load_data(data)

def work_parallel(data, thread_number=4):
    pool = ThreadPool(thread_number)
    results = pool.map(thread_worker, data)

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    data = create_dataframe(50000)
    num_cores = cpu_count() - 1
    df_split = np.array_split(data, num_cores)

    S = scoped_session(Session)

    work_parallel(df_split, num_cores)

    S.remove()
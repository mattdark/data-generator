from multiprocessing import Pool
from multiprocessing import cpu_count
import pandas as pd
from pymongo import MongoClient
from modules.dataframe import create_dataframe

if __name__ == "__main__":
    num_cores = cpu_count() - 1
    with Pool() as pool:
        data = pd.concat(pool.map(create_dataframe, range(num_cores)))
    data_dict = data.to_dict('records')
    uri = "mongodb://user:password@localhost:27017/company?authSource=admin"
    client = MongoClient(uri)
    db = client["company"]

    collection = db["employees"]
    collection.insert_many(data_dict)
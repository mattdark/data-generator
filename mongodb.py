from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
import json
import pandas as pd
from tqdm import tqdm
from faker import Faker
from pymongo import MongoClient
from modules.dataframe import create_dataframe

if __name__ == "__main__":
    data = create_dataframe(50000)
    data_dict = data.to_dict('records')
    uri = "mongodb://user:password@localhost:27017/company?authSource=admin"
    client = MongoClient(uri)
    db = client["company"]

    collection = db["employees"]
    collection.insert_many(data_dict)
from multiprocessing import Pool, cpu_count

import pandas as pd
from sqlalchemy import text

from modules.dataframe import create_dataframe
from modules.schema import schema
from modules.base import get_client

if __name__ == "__main__":
    num_cores = cpu_count() if cpu_count() <= 2 else cpu_count() - 1
    
    db_type, client = get_client()
    
    with Pool(processes=num_cores) as pool:
        data = pd.concat(pool.map(create_dataframe, range(num_cores)))

    if db_type in {"mysql", "postgres"}:
        data.to_sql(name='employees', con=client, if_exists='append', index=False, dtype=schema)
    
        with client.begin() as conn:
            if db_type == "mysql":
                conn.execute(text("ALTER TABLE employees ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;"))
            elif db_type == "postgres":
                conn.execute(text("ALTER TABLE employees ADD COLUMN id SERIAL PRIMARY KEY;"))
    elif db_type == "mongodb":
        data_dict = data.to_dict('records')
        db = client["company"]
        collection = db["employees"]
        collection.insert_many(data_dict)
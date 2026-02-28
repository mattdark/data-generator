from multiprocessing import Pool, cpu_count

import pandas as pd
from sqlalchemy import text

from modules.dataframe import create_dataframe
from modules.schema import schema
from modules.base import Session, engine


if __name__ == "__main__":
    num_cores = cpu_count() if cpu_count() <= 2 else cpu_count() - 1
    
    with Pool(processes=num_cores) as pool:
        data = pd.concat(pool.map(create_dataframe, range(num_cores)))

    data.to_sql(name='employees', con=engine, if_exists='append', index=False, dtype=schema)
    
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE employees ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;"))
        # conn.execute("ALTER TABLE employees ADD COLUMN id SERIAL PRIMARY KEY;")
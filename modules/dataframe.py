from multiprocessing import cpu_count
import pandas as pd
from tqdm import tqdm
from faker import Faker

fake = Faker()

num_cores = cpu_count() - 1
def create_dataframe(arg):
    x = int(60000/num_cores)
    data = pd.DataFrame()
    for i in tqdm(range(x), desc='Creating DataFrame'):
        data.loc[i, 'first_name'] = fake.first_name()
        data.loc[i, 'last_name'] = fake.last_name()
        data.loc[i, 'job'] = fake.job()
        data.loc[i, 'address'] = fake.address()
        data.loc[i, 'city'] = fake.city()
        data.loc[i, 'email'] = fake.email()
    return data
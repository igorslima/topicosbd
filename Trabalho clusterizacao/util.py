import pandas as pd
from DAO.verticeDAO import *
def join_all_files(hora):
    df = pd.DataFrame()
    df['id_taxista'] = 0
    df['date_time'] = 0
    df['longitude'] = 0
    df['latitude'] = 0
    

    return df

data = join_all_files('oi')
print(type(data))
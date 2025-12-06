import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    return df.copy()
# print(load_csv('data_pipeline_project/SuperMarketData.csv'))

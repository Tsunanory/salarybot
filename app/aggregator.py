import pymongo
import pandas as pd
from datetime import datetime


def aggregate_salaries(dt_from, dt_upto, group_type):

    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['salary_aggregation_db']
    collection = db['salaries']


    dt_from = datetime.fromisoformat(dt_from)
    dt_upto = datetime.fromisoformat(dt_upto)


    data = collection.find({"dt": {"$gte": dt_from, "$lte": dt_upto}})

    df = pd.DataFrame(list(data))
    print(df.head())


    if 'dt' not in df.columns or 'value' not in df.columns:
        raise KeyError("The 'dt' or 'value' column is missing from the data.")

    if group_type == 'hour':
        df['dt'] = pd.to_datetime(df['dt']).dt.floor('h')
    elif group_type == 'day':
        df['dt'] = pd.to_datetime(df['dt']).dt.floor('D')
    elif group_type == 'month':
        df['dt'] = pd.to_datetime(df['dt']).dt.to_period('M').dt.to_timestamp()
    else:
        raise ValueError("Invalid group_type. Choose from 'hour', 'day', or 'month'")

    grouped = df.groupby('dt')['value'].sum().reset_index()

    dataset = grouped['value'].tolist()
    labels = grouped['dt'].dt.strftime('%Y-%m-%dT%H:%M:%S').tolist()

    return {"dataset": dataset, "labels": labels}


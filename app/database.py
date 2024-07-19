from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['salary_aggregation_db']
collection = db['salaries']


def get_collection():
    return collection

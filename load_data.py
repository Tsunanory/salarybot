import pymongo
import bson


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['salary_aggregation_db']
collection = db['salaries']


with open('data/sample_collection.bson', 'rb') as f:
    data = bson.decode_all(f.read())


collection.insert_many(data)

print("Data inserted successfully")

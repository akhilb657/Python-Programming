from pymongo import MongoClient

client = MongoClient("localhost",27017)

database = client['mydb']


collection = database['product']

collection.delete_one({"name":"Mac"})

cursor = collection.find({"name":"Mac"})
for each_doc in cursor:
    print(each_doc)
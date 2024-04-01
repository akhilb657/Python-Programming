from pymongo import MongoClient

client = MongoClient("localhost",27017)

database = client['mydb']


collection = database['product']

filter = {"name":"Iphone"}
res = collection.update_many(filter,{"$set":{"price":1100}})

print(res.modified_count)

cursor = collection.find({"name":"Iphone"})
for each_doc in cursor:
    print(each_doc)
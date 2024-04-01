from pymongo import MongoClient

client = MongoClient("localhost",27017)

database = client['mydb']

print("Database created")

collection = database['product']

print("Collection created")

products = [{
    "name":"Iphone",
    "price":900
},
    {
        "name": "Mac",
        "price": 1900
    },
    {
        "name":"DELL",
        "price":1500
    }
]
res = collection.insert_many(products)
print(res.inserted_ids)


from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.vfvavqz.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)   # connect to mongodb

db = client.pytech  # connect to pytech database

print(db.list_collection_names())   # list all collections

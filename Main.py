from pymongo import MongoClient

client = MongoClient("localhost")
db = client["test_database"]

productcol = db['product_data']
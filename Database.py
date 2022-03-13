
from msilib.schema import Error
from pymongo import MongoClient, collection
import psycopg2

class Database:
    def __init__(self, dbname):
        # self.mongoClient = MongoClient("mongodb+srv://daniloDbUser:Joeydanilo1%21@danilo.sxj7r.gcp.mongodb.net/aigp?authSource=admin&replicaSet=Danilo-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
        self.mongoClient = MongoClient("localhost")
        self.mongodb = self.mongoClient["test_database"]

        self.postgres = psycopg2.connect(
                host="localhost",
                dbname=dbname,
                user="postgres",
                password="admin"
            )
    
    #Getting data from a mongodb collection
    def findMongoData(self, collection: collection.Collection, *props):
        # id, name, price, cat1, cat2, recommendable, sm:active, properties:av_store, properties: av_warehouse

        options = {}

        #create option dict
        for key in props:
            options[key] = 1
        print(options)

        #Get data from collection
        # for x in self.db['products'].find({"_id": "100092"}):
        #     print(x)
        collection.find()
        return collection
        # return collection.find_one({"_id": "100241"})

    def insertData(self):
        return
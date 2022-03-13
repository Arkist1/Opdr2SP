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
        self.connections = {}
    
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

    def updatedata(self):
        self.cleardb()
        
        dbname = self.mongodb.name
        print("Connected tot", dbname)
        
        self.updateproducts()
        self.updateprofiles()
        self.updatesessions()
        self.updateconnections()
        
    def updateproducts(self):
        products = self.mongodb['product_data']

        for product in products.find():
            data = {}
            data["id"] = product["_id"]
            data["naam"] = self.fix_string(product["name"])
            data["brand"] = self.fix_string(product["brand"])
            data["prijs"] = product["price"]["selling_price"]
            data["category_1"] = self.fix_string(product["category"]["category_1"])
            data["category_2"] = self.fix_string(product["category"]["category_2"])
            
            properties = product["properties"]
            data["ava_store"] = properties["availability_store"] if properties["availability_store"] != "" else 0
            data["ava_warehouse"] = int(properties["availability_warehouse"])
            data["recommendable"] = product["recommendable"]
            data["is_active"] = product["sm"]["is_active"]
            
            cur = self.postgres.cursor()
            cur.execute(f"INSERT INTO product_data(id, naam, prijs, brand, category_1, category_2, "
                                  f"availabity_store, availibility_warehouse, recommendable, active)"
                                  f"VALUES({data['id']}, '{data['naam']}', {data['prijs']}, '{data['brand']}', '{data['category_1']}',"
                                  f"'{data['category_2']}', {data['ava_store']}, {data['ava_warehouse']}, {data['recommendable']}, {data['is_active']})")
        
    def updateprofiles(self):
        profilescol = self.mongodb['profiles']
        
        for profile in profilescol.find():
            data = {"created_at": profile["sm"]["created"]["$date"],
                    "id": profile["_id"]}
            
            for x in profile["buids"]:
                self.connections["x"] = data[id]
                
            cur = self.postgres.cursor()
            cur.execute(f"INSER INTO profile (id, created_at) VALUES({data['id']}, '{data['created_at']}')")
        
        
        self.postgres.commit()

    def updatesessions(self):
        sessionscol = self.mongodb['sessions']
        
    def updateconnections(self):
        return
    
    def insertData(self):
        return
    
    def cleardb(self):
        cur = self.postgres.cursor()
        with open("sql.txt", "r") as f:
            cur.execute(f.read())
        self.postgres.commit

    def fix_string(self, string):
        return self.replace_space(self.replace_apos(string))
    
    def replace_space(self, string):
        return "".join(["_" if x == " " else x for x in string])
    
    def replace_apos(self, string):
        return "".join(["_" if x == "'" else x for x in string])

    
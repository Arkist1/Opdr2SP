from Database import Database

def updatedata(db):

    dbname = db.name
    print ("Connected tot %s", dbname)
    # db = client["test_database"]
    
    products = db.get_collection('products')
    for product in products:
        print(product)
    
    # sessioncol = db['anonymous_sessions']
    # profilescol = db['anonymous_profiles']
    
    

database = Database("test_database")
print(database.findMongoData(database.db.get_collection('products'), '_id', 'name'))

if __name__ == '__main__':
    updatedata(database.db)
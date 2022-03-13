from Database import Database

def updatedata(db):

    dbname = db.name
    print ("Connected tot", dbname)
    # db = client["test_database"]
    
    products = db['product_data']
    for product in products.find():
        print(product)
    
    # sessioncol = db['anonymous_sessions']
    # profilescol = db['anonymous_profiles']

if __name__ == '__main__':
    database = Database("RecommendationEngine")
    
    updatedata(database.mongodb)
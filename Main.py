from pymongo import MongoClient
import psycopg2


def updatedata():
    client = MongoClient("localhost")
    db = client["test_database"]
    
    productcol = db['product_data']
    sessioncol = db['anonymous_sessions']
    profilescol = db['anonymous_profiles']
    
    


if __name__ == '__main__':
    updatedata()
from pymongo import MongoClient
import psycopg2


def connectpostgres(dbname):
    conn = psycopg2.connect(
        host="localhost",
        dbname=dbname,
        user="postgres",
        password="admin"
    )
    
    return conn


def updatedata():
    postgres = psycopg2.connect("dbname=RecommendationEngine password=admin")
    client = MongoClient("localhost")
    db = client["test_database"]
    
    productcol = db['product_data']
    sessioncol = db['anonymous_sessions']
    profilescol = db['anonymous_profiles']
    
    


if __name__ == '__main__':
    updatedata()
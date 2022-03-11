import psycopg2

con = psycopg2.connect(             #verbinding maken met de database
    host = 'localhost',
    database = 'huwebshop',         #pas eigen instellingen hier aan
    user = 'postgres',
    password= 'snellestijn')

cur = con.cursor()

def productpakken():
    #code die een product returned op basis van de parameters waaraan die moet voldoen
    
    cur.execute("select * from voorwerp;")
    alles = cur.fetchall()
    print(alles)

    pass


def productneerzetten(id,naam):
    #code die een bepaald product in de database zet
    cur.execute("insert into voorwerp values (%s,%s);",(id,naam))
    con.commit()
    pass




productpakken()
productneerzetten('123','handschoen')





cur.close()
con.close()
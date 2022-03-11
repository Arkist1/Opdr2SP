import psycopg2

con = psycopg2.connect(             #verbinding maken met de database
    host = 'localhost',
    database = 'huwebshop',         #pas eigen instellingen hier aan
    user = 'postgres',
    password= 'snellestijn')
cur = con.cursor()



#code die een bepaald product in de database zet
def productneerzetten(id,naam,prijs,cat1,cat2,aanraadbaar,actief,inwinkel,inopslag):
    cur.execute("insert into voorwerp values (%s,%s,%s,%s,%s,%s,%s,%s,%s);",(id,naam,prijs,cat1,cat2,aanraadbaar,actief,inwinkel,inopslag))
    con.commit()

#voorbeeld van wat er toegevoegd kan worden aan de database in postgres
productneerzetten('12677','auto','3.90','speelgoed','kinderen',True,True,True,True)



#stukje om te table te weergeven in terminal
cur.execute("select * from voorwerp;")
print(cur.fetchall())



#afsluiten van de verbinding, om fouten te verkomen
cur.close()
con.close()
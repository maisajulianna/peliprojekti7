#8.1
print()
print("tehtävä 1")
print()

# ohjelma kysyy käyttäjältä maakoodin
# ohjelma tulostaa maan lentokenttien lukumäärät tyypeittäin

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,        #mysql-portti
    database='flight_game',
    user="user2",
    password="pass2word_",
    autocommit=True
    )


def airports_by_type(maakoodi):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{maakoodi}'" +\
          " group by type"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    return result

# pääohjelma

maakoodi = input("Anna maakoodi: ")

alltypes = airports_by_type(maakoodi)
print(alltypes)
print()
(f"Maakoodilla {maakoodi} löytyi seuraavia lentokenttätyyppejä:")

print()
times = 0

for type in alltypes:
    bytype = alltypes[times]
    print(f"Tyyppiä {bytype[0]} on {bytype[1]}.")
    times = times + 1


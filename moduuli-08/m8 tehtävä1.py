#8.1
print()
print("tehtävä 1")
print()

# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin
# ohjelma hakee ja tulostaa lentokentän nimen ja sijaintikunnan
# koodi on tallennettuna airport-taulun ident-sarakkeeseen

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,        #mysql-portti
    database='flight_game',
    user="user2",
    password="pass2word_",
    autocommit=True
    )


def find_airport(ident):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{ident}'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    # print(result)
    if cursor.rowcount > 0:
        return result
    else:
        return "Ei tuloksia"

# pääohjelma

ident = input("Anna lentokentän ICAO-koodi: ")

print()
result = find_airport(ident)
print(f"Lentokentän nimi on {result[0]}. Se sijaitsee paikassa {result[1]}.")

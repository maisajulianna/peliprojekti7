print()
print("Hei!")
player = input("Anna pelaajasi nimi: ")
print()
print(f"Tervetuloa {player}!")
print()

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user="user2",
    password="pass2word_",
    autocommit=True
    )

def choose_plane():
    chosen = False
    while chosen == False:
        print("Minkä lentokoneen haluaisit valita?")
        print()
        print("Vaihtoehdot:")
        print("1: Vähäpäästöinen matkustajakone")
        print("2: Normaali matkustajakone")
        print("3: Yksityiskone")
        print("4: Hävittäjä")
        print()
        plane = int(input("Valitsemasi lentokoneen numero: "))
        print()
        chosen = True
        if plane == 1:
            print("jotain")
        elif plane == 2:
            print("jotain muuta")
        elif plane == 3:
            print("en tiiä")
        elif plane == 4:
            print("...")
        else:
            print()
            print("Virheellinen arvo.")
            again = int(input("Paina 1, jos haluat valita uudestaan: "))
            print()
            if again == 1:
                chosen = False
            else:
                print("Lopetit pelin.")
                break


def choose_start():
    print("Seuraavaksi saat valita lentokentän, jolta aloitat pelin.")
    sql = f"SELECT name, iso_country FROM airport WHERE type = 'large_airport'" +\
        "WHERE iso_country = ''"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    times = 0
    print("Lentokenttävaihtoehdot:")
    print()
    for result in result:
        byname = result[times]
        print(f"Lentokenttä {byname[0]} maassa {byname[1]}.")
        times = times + 1
    print(result)








choose_plane()
choose_start()
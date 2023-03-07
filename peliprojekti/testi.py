import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user="userN",
    password="1234",
    autocommit=True)


def continent_name(continent_abbr):
    if continent_abbr == 'AF':
        continent = "Afrikka"
    elif continent_abbr == 'EU':
        continent = "Eurooppa"
    elif continent_abbr == 'NA':
        continent = "Pohjois-Amerikka"
    elif continent_abbr == 'SA':
        continent = "Etelä-Amerikka"
    elif continent_abbr == 'OC':
        continent = "Australia ja Oseania"
    elif continent_abbr == 'AS':
        continent = "Aasia"
    elif continent_abbr == 'AN':
        continent = "Antarktika"
    return continent


def choose_continent():
    print()
    print("Mihin haluaisit lentää?")
    print()
    print("Valitse aluksi maanosa: ")
    sql = f"SELECT continent FROM airport GROUP BY continent"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    continents = cursor.fetchall()
    # print(continents)

    chosen = False
    while chosen == False:
        gameover1 = False
        times = 0
        id = 1
        for i in continents:
            one = continents[times]
            continent_abbr = one[0]
            continent = continent_name(continent_abbr)
            print(f"{id}: {continent}")
            times += 1
            id += 1

        print()
        continentNro = int(input("Haluamasi maanosan numero: "))
        to_continent = 0

        if continentNro >= 1 and continentNro <= 7:
            index = continentNro - 1
            continents = continents[index]
            to_continent = continents[0]
            continent = continent_name(to_continent)
            print(f"Valitsemasi maanosa on {continent}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vaan numeroa jos haluat lopettaa.")
            again = int(input("Paina 1, jos haluat valita uudestaan: "))
            print()
            if again == 1:
                print()
                print("Vaihdoehdot uudestaan:")
                chosen = False
            else:
                print("Lopetit pelin.")
                chosen = True
                gameover1 = True

        if continentNro >= 1 and continentNro <=7 :
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter.")
            if confirmation == "":
                print("Maanosa valittu!")
                chosen = True
            else:
                print()
                print("Valitse uudestaan:")
                chosen = False
    return to_continent, gameover1


def choose_country():
    print()
    print("Valitse seuraavaksi maa.")
    print()
    print("Valitsemasi maanosan maiden ISO-koodit:")

    sql = f"SELECT iso_country FROM airport WHERE continent = '{to_continent}' GROUP BY iso_country"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    # print(countries)

    gameover2 = False
    chosen = False
    while chosen == False:
        times = 0
        id = 1
        for i in countries:
            one = countries[times]
            country = one[0]
            print(f"{id}: {country}")
            times += 1
            id += 1

        print()
        countryNro = int(input("Haluamasi maan numero: "))
        to_country = 0
        list_index = len(countries)
        print(list_index)

        if countryNro >= 1 and countryNro <= list_index:
            index = countryNro - 1
            countries = countries[index]
            to_country = countries[0]
            print(f"Valitsemasi maa on {to_country}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vaan numeroa jos haluat lopettaa.")
            again = int(input("Paina 1, jos haluat valita uudestaan: "))
            print()
            if again == 1:
                print()
                print("Vaihdoehdot uudestaan:")
                chosen = False
            else:
                print("Lopetit pelin.")
                gameover2 = True

        if countryNro >= 1 and countryNro <= 60:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter.")
            if confirmation == "":
                print("Maa valittu!")
                chosen = True
            else:
                print()
                print("Valitse uudestaan:")
                chosen = False
    return to_country, gameover2


def choose_municipality():
    print()
    print("Valitse seuraavaksi kaupunki.")
    print()
    print("Valitsemasi maan kaupungit, joissa on lentokenttä:")

    sql = f"SELECT municipality, type FROM airport WHERE iso_country = '{country}' " \
          f"or type = 'large_airport' or type = 'medium_airport' " \
          f"or type = 'small_airport' GROUP BY municipality"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    municipalities = cursor.fetchall()
    # print(municipalities)

    gameover3 = False
    chosen = False
    while chosen == False:
        times = 0
        id = 1
        for i in municipalities:
            one = municipalities[times]
            municipality = one[0]
            print(f"{id}: {municipality}")
            times += 1
            id += 1

        print()
        municipalityNro = int(input("Haluamasi kaupungin numero: "))
        municipality = 0
        list_index = len(municipalities)
        print(list_index)

        if municipalityNro >= 1 and municipalityNro <= list_index:
            index = municipalityNro - 1
            municipalities = municipalities[index]
            municipality = municipalities[0]
            print(f"Valitsemasi maa on {municipality}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vaan numeroa jos haluat lopettaa.")
            again = int(input("Paina 1, jos haluat valita uudestaan: "))
            print()
            if again == 1:
                print()
                print("Vaihdoehdot uudestaan:")
                chosen = False
            else:
                print("Lopetit pelin.")
                gameover3 = True

        if municipalityNro >= 1:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter.")
            if confirmation == "":
                print("Kaupunki valittu!")
                chosen = True
            else:
                print()
                print("Valitse uudestaan:")
                chosen = False
    return municipality, gameover3


def travel():
    to_continent = choose_continent()
    choose_country()
    choose_municipality()
    to_airport = choose_airport



# -- -- -- pääohjelma -- -- --

gameover = False

while gameover == False:
    result = choose_continent()
    to_continent = result[0]
    gameover = result[1]
    if gameover == True:
        break

    result = choose_country()
    country = result[0]
    gameover = result[1]
    gameover = result[1]
    if gameover == True:
        break

    result = choose_municipality()
    municipality = result[0]
    gameover = result[1]
    if gameover == True:
        break

    # choose_airport()

print("Peli loppui.")
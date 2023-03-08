def continent_name(continent_abbr):
    if continent_abbr == 'AF':
        continent_fi = "Afrikka"
    elif continent_abbr == 'EU':
        continent_fi = "Eurooppa"
    elif continent_abbr == 'NA':
        continent_fi = "Pohjois-Amerikka"
    elif continent_abbr == 'SA':
        continent_fi = "Etelä-Amerikka"
    elif continent_abbr == 'OC':
        continent_fi = "Australia ja Oseania"
    elif continent_abbr == 'AS':
        continent_fi = "Aasia"
    elif continent_abbr == 'AN':
        continent_fi = "Antarktika"
    return continent_fi


def choose_continent():
    sql = f"SELECT continent FROM airport GROUP BY continent"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    continents = cursor.fetchall()
    # print(continents)

    print()
    print("Mihin haluaisit lentää?")
    print()
    print("Valitse aluksi maanosa: ")

    times = 0
    id = 1
    for i in continents:
        one = continents[times]
        continent_abbr = one[0]
        continenT = continent_name(continent_abbr)
        print(f"{id}: {continenT}")
        times += 1
        id += 1

    chosen = False
    while chosen == False:
        gameover1 = False
        print()
        continentNro = int(input("Haluamasi maanosan numero: "))
        continentA = 0

        if continentNro >= 1 and continentNro <= 7:
            index = continentNro - 1
            continents = continents[index]
            continentA = continents[0]
            continent = continent_name(continentA)
            print(f"Valitsemasi maanosa on {continent}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan. ")
            if again == "":
                chosen = False
            else:
                print()
                print("Lopetit pelin.")
                chosen = True
                gameover1 = True

        if continentNro >= 1 and continentNro <=7 :
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Maanosa valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT continent FROM airport GROUP BY continent"
                cursor = connection.cursor()
                cursor.execute(sql)
                continents = cursor.fetchall()
    return continentA, gameover1


def choose_country(to_continent):
    print()
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

    times = 0
    id = 1
    for i in countries:
        one = countries[times]
        country = one[0]
        print(f"{id}: {country}")
        times += 1
        id += 1

    chosen = False
    while chosen == False:
        gameover2 = False
        print()
        countryNro = int(input("Haluamasi maan numero: "))
        to_country = 0
        list_index = len(countries)
        # print(list_index)

        if countryNro >= 1 and countryNro <= list_index:
            index = countryNro - 1
            countries = countries[index]
            to_country = countries[0]
            print(f"Valitsemasi maa on {to_country}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print()
                print("Lopetit pelin.")
                chosen = True
                gameover2 = True

        if countryNro >= 1 and countryNro <= list_index:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Maa valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT iso_country FROM airport WHERE continent = '{to_continent}' GROUP BY iso_country"
                cursor = connection.cursor()
                cursor.execute(sql)
                countries = cursor.fetchall()
    return to_country, gameover2


def choose_municipality(to_country):
    print()
    print("Valitse seuraavaksi kaupunki.")
    print()
    print("Valitsemasi maan kaupungit, joissa on lentokenttä:")

    sql = f"SELECT municipality, type FROM airport WHERE iso_country = '{to_country}' " \
          f"AND type = 'large_airport' OR iso_country = '{to_country}' " \
          f"AND type = 'medium_airport' OR iso_country = '{to_country}' " \
          f"AND type = 'small_airport' GROUP BY municipality"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    municipalities = cursor.fetchall()
    # print(municipalities)
    print()

    gameover3 = False
    chosen = False
    while chosen == False:
        times = 0
        id = 1

        for i in municipalities:
            #if times != 0:
            one = municipalities[times]
            municipality = one[0]
            print(f"{id}: {municipality}")
            id += 1
            times += 1


        print()
        list_index = (len(municipalities)) - 1
        #print(list_index)
        municipalityNro = int(input("Haluamasi kaupungin numero: "))
        municipality = 0

        if municipalityNro >= 1 and municipalityNro <= list_index+1:
            index = municipalityNro - 1
            m = municipalities[index]
            municipality = m[0]
            print(f"Valitsemasi kaupunki on {municipality}.")
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


def choose_airport(municipality):
    print()
    print("Valitse vielä lentokenttä.")
    print()
    print("Lentokentät valitsemassasi kaupungissa:")

    sql = f"SELECT name, ident, type FROM airport WHERE municipality = '{municipality}' " \
          f"AND type = 'large_airport' OR municipality = '{municipality}' " \
          f"AND type = 'medium_airport' OR municipality = '{municipality}' " \
          f"AND type = 'small_airport' ORDER BY type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    airports_list = cursor.fetchall()
    print(airports_list)
    print()

    gameover4 = False
    chosen = False
    while chosen == False:
        times = 0
        id = 1

        for i in airports_list:
            one = airports_list[times]
            airport_name = one[0]
            airport_type = one[2]
            print(f"{id}: {airport_name}, tyyppiä {airport_type}")
            id += 1
            times += 1


        print()
        list_index = (len(airports_list)) - 1
        print(list_index)
        airportNro = int(input("Haluamasi lentokentän numero: "))
        airport = 0

        if airportNro >= 1 and airportNro <= list_index:
            index = airportNro - 1
            airports_list = airports_list[index]
            airport = airports_list[0]
            airport_ident = airports_list[1]
            print(f"Valitsemasi lentokenttä on {airport}.")
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
                gameover4 = True

        if airportNro >= 1:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter.")
            if confirmation == "":
                print("Lentokenttä valittu!")
                chosen = True
            else:
                print()
                print("Valitse uudestaan:")
                chosen = False
    return airport, airport_ident, gameover4


def travel():
    gameover_main = False
    while gameover_main == False:
        result = choose_continent()
        to_continent = result[0]
        print(result)
        a = input("press enter to continue")
        gameover_main = result[1]
        if gameover_main == True:
            break

        result = choose_country(to_continent)
        to_country = result[0]
        gameover_main = result[1]
        if gameover_main == True:
            break

        result = choose_municipality(to_country)
        municipality = result[0]
        gameover_main = result[1]
        if gameover_main == True:
            break

        result = choose_airport(municipality)
        to_airport = result[0]
        airport_ident = result[1]
        gameover_main = result[2]

    return to_airport, to_continent, gameover_main




# -- -- -- pääohjelma -- -- --
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user="userN",
    password="1234",
    autocommit=True)

to_airport = " "
result = travel()
travel_airport = result[0]
travel_continent = result[2]

print("Peli loppui.")
print()
print("Hei!")
player = input("Anna pelaajasi nimi: ")
print()
print(f"Tervetuloa {player}!")
print()


def choose_plane():
    chosen = False
    while chosen == False:
        print("Minkä lentokoneen haluaisit valita?")
        print("Vaihtoehdot:")
        print("1: Normaali matkustajakone")
        print("2: Vähäpäästöinen matkustajakone")
        print("3: Yksityiskone")
        print("4: Hävittäjä")
        plane = int(input("Valitsemasi lentokoneen numero: "))
        chosen = True
        if plane == 1:
            print("jotain")
        elif plane == 2:
            print("jotain muuta")
        elif plane == 3:
            print("en tiiä")
        elif plane == 4:
            ("...")
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

choose_plane()
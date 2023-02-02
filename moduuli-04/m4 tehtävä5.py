#4.5
print()
print("tehtävä 5")
print()

username = input("Käyttäjätunnus: ")
password = input("Salasana: ")

times = 5

while username != "python" or password != "rules":
    print()
    print("Pääsy evätty. Yritä uudelleen:")
    username = input("Käyttäjätunnus: ")
    password = input("Salasana: ")
    times = times - 1
    if times == 1:
        print()
        print("Yrityksesi loppuivat.")
        break

if username == "python" and password == "rules":
    print()
    print("Tervetuloa!")
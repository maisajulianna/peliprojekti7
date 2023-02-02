#4.3
print()
print("tehtävä 3")
print()

suurin = 0
pienin = 0

luku = input("Anna luku, tyhjä lopettaa: ")

if luku != "":
    pienin = suurin = int(luku)

print()
while luku != "":
    luku = int(luku)
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku
    luku = input("Anna uusi luku: ")

if luku == "":
    print()
    print("Suurin luvuista on", suurin, "ja pienin on", pienin, ".")

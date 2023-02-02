#6.4
print()
print("tehtävä4")
print()

# funktio saa parametrinaan listan kokonaislukuja
# funktio palauttaa listassa olevien lukujen summan
# pääohjelma luo listan, kutsuu funktiota ja tulostaa sen palauttaman summan


def summa(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa

luvut = [1,2,3,4,5,6,7,8,9]

result = summa(luvut)
print(f"Listan lukujen summa on {result}.")
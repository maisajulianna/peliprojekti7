#6.5
print()
print("tehtävä 5")
print()

# funktio saa parametrinaan listan kokonaislukuja
# ohjelma palauttaa listan, jossa on vain annetun listan parilliset luvut
# pääohjelma luo lista, kutsuu funktiota ja tulostaa molemmat listat

def even(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

lista = [2,3,4,5,8,9,12,13,14]

result = even(lista)
print(f"Alkuperäinen lista: {lista}")
print(f"Listan parilliset luvut: {result}")

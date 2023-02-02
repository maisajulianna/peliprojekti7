#2.4
print()
print("tehtävä 4")
#input 3 kokonaislukua, print summa, tulo ja keskiarvo

print()
print("kirjoita kolme kokonaislukua:")
luku1_str = input("luku1: ")
luku2_str = input("luku2: ")
luku3_str = input("luku3: ")

luku1 = float(luku1_str)
luku2 = float(luku2_str)
luku3 = float(luku3_str)

sum = (luku1 + luku2 + luku3)
product = (luku1 * luku2 * luku3)
mean = ((luku1 * luku2 * luku3)/3)

print()
print("kokonaislukujen summa on: " + str(sum))
print("kokonaislukujen tulo on: " + str(product))
print("kokonaislukujen keskiarvo on: " + str(round(mean, 5)))
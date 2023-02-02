# luvun arvon testaus if-lauseella:

print()
luku = float(input("Anna luku: "))

if luku > 0:
    print("Luku on positiivinen.")
elif luku < 0:
    print("Luku on negatiivinen.")
elif luku == 0:
    print("Luku on nolla.")
else:
    print("error")

# parempi:

luku = float(input("Anna luku: "))

if luku > 0:
    print("Luku on positiivinen.")
elif luku < 0:
    print("Luku on negatiivinen.")
else:
    print("Luku on nolla.")
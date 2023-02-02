#3.2
print("tehtävä 2")
print()

hytti = input("Anna hyttiluokka: ")
print()

if hytti == "LUX" or "Lux" or "lux":
    print("Parvekkeellinen hytti sijaitsee yläkannella.")

elif hytti == "A" or "a":
    print("Ikkunallinen hytti on autokannen yläpuolella")

elif hytti == "B" or "b":
    print("Ikkunaton hytti on autokannen yläpuolella")

elif hytti == "C" or "c":
    print("Ikkunaot hytti on autokannen alapuolella")

else:
    print("Virheellinen hyttiluokka")
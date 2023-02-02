#4.6
print()
print("tehtävä 6")
print()
import random

N = 1000000
counter = 0
# n = ympyrän sisällä olevat pisteet
n = 0

while counter < N:
    counter = counter + 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    # print(f"Arvottu piste: {x}, {y}")
    # onko piste yksikköympyrän sisällä; x^2+y^2<1
    if x * x + y * y < 1:
        # print("Piste on ympyrän sisällä.")
        n += 1
print(f"Pisteitä arvottu yhteensä {counter}, joista {n} kpl on ympyrän sisällä.")

pii = 4 * n / N
print("Arvottujen pisteiden perusteella piin likiarvo on", pii)
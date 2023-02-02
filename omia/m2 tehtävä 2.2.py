#2.2.2
print()
print("tehtävä 2")
print()

import math

säde = input("lisää ympyrän säde: ")
print()

säde = float(säde)

C = (math.pi) * säde ** 2
print("ympyrän pinta-ala on: " + str(round(C,3)))

print(f"Ympyrän pinta-ala on: {C:.3f}")
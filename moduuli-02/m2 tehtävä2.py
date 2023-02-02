#2.2

import math

print()
print("tehtävä 2")
print()

r_str = input("lisää ympyrän säde: ")
print()

r = float(r_str)

C = (math.pi) * r ** 2
print("ympyrän pinta-ala on: " + str(round(C,3)))
#2.5
print()
print("tehtävä 5")
import math

# input leiviskät, naulat, luodit
#print kilot ja grammat

print()
leiviskät_str = input("anna leiviskät: ")
naulat_str = input("anna naulat: ")
luodit_str = input("anna luodit: ")

leiviskät = float(leiviskät_str)
naulat = float(naulat_str)
luodit = float(luodit_str)

grammat = ((luodit * 13.3) + (naulat * 32 * 13.3) + (leiviskät * 20 * 32 * 13.3))
kilot = math.floor(grammat/1000)
jakojäännös = (grammat - kilot * 1000)

print()
print(f"massa nykymittojen mukaan on: " + str(kilot) + " kiloa ja " + str(round(jakojäännös, 1)) + " grammaa")
# 39,9 + 3404,8 + 42560
# 66,5 + 1596 + 51072
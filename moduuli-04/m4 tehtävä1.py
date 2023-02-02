#4.1
print()
print("tehtävä 1")
print()

#tulosta kolmella jaolliset luvut väliltä 1 - 1000

print("3:lla jaolliset luvut 1000 asti:")
print()

number = 1

while number < 1000:
    number += 1
    if number % 3 == 0:
        print("Luku" , number, "on jaollinen kolmella.")

#2.6
print()
print("tehtävä 6")

import random

#kolmenumeroinen koodi, numerot väliltä 0-9:

randomnumber1 = random.randint(0,9)
randomnumber2 = random.randint(0,9)
randomnumber3 = random.randint(0,9)

code = str(randomnumber1) + str(randomnumber2) + str(randomnumber3)

print("numerolukon koodi on: " + code)


#nelinumeroinen koodi, numerot väliltä 1-6:

randomnumber1 = random.randint(0,6)
randomnumber2 = random.randint(0,6)
randomnumber3 = random.randint(0,6)
randomnumber4 = random.randint(0,6)

code = str(randomnumber1) + str(randomnumber2) + str(randomnumber3) + str(randomnumber4)

print("numerolukon koodi on: " + code)
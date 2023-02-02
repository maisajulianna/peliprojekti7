#4.6
print()
print("tehtävä 6")
print()
import random

#algoritmi piin likiarvon laskemiseksi

# A = yksikköympyrä, keskipiste origossa, säde 1
# B = pienin mahdollinen neliö, jonka sisälle A mahtuu
# B: nurkkapisteet on (-1,-1)(1,-1)(1,1) ja (-1,1)

# arvotaan neliön sisälle pisteitä

x = random.uniform(-1,1)
y = random.uniform(-1,1)

print(f"Arvottu piste: {x}, {y}")
# onko piste yksikköympyrän sisällä; x^2+y^2<1
if x * x + y * y < 1:
    print("Piste on ympyrän sisällä.")
else:
    print("Piste ei ole ympyrän sisällä.")
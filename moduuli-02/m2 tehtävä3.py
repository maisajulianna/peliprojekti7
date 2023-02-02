#2.3
print()
print("tehtävä 3")
print()
#input kanta(a) ja  korkeus(h) → print piiri(p) ja pinta-ala(A)
a_str = input("lisää suorakulmion kanta: ")
h_str = input("lisää suorakulmion korkeus: ")

a = float(a_str)
h = float(h_str)

p = (2*a+2*h)
A = (a*h)

print()
print("suorakulmion piiri on: " + str(p))
print("suorakulmion pinta-ala on: " + str(A))
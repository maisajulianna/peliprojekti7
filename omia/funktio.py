# funktio korottaa luvut potenssiin

def power(num,pow):
    result = num**pow
    return result

print()
luku = int(input("Anna kantaluku: "))
eksp = int(input("Anna eksponentti: "))

result = power(luku,eksp)

print(f"{luku} korotettuna potenssiin {eksp} on {result}.")


# toinen tapa

print(f"Tulos on {power(luku, eksp)}")
print(f"Tulos on {power(5,2)}")
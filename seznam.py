seznam = []

while True:
    x = int(input("Zadejte cislo do seznamu (ukoncit 0): "))
    if x == 0:
        break
    else:
        seznam.append(x)

if seznam:
    minimum = seznam[0]
    maximum = seznam[0]
    
    for cislo in seznam:
        if cislo < minimum:
            minimum = cislo
        if cislo > maximum:
            maximum = cislo
    
    print(f"Seznam: {seznam}")
    print(f"Minimální číslo: {minimum}")
    print(f"Maximální číslo: {maximum}")
else:
    print("Seznam je prázdný.")

#import math
"""print("Zjistovac prvocisel")

n=int(input("Zadej cislo:"))

def je_prvocislo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if(je_prvocislo(n)==True):
    print("JE prvocislo")
else:
    print("NENI prvocislo")


import math
def je_prvocislo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
print("Zjistovac prvocisel")

od=int(input("Zadej od jakeho cisla:"))
do=int(input("Zadej po jake cislo:"))

for i in range(od,do+1,1):
    if je_prvocislo(i)==True:
        print (i,end=" ")

"""
#import math

bankovky = [2000, 1000, 500, 200, 100]  # Seřazeno sestupně
mince = [50, 20, 10, 5, 2, 1]           # Seřazeno sestupně
rozmeneni = []

suma = int(input("Kolik penez chcete vybrat?: "))

while suma > 0:
    if suma >= 100:  # Práce s bankovkami
        for bankovka in bankovky:
            while suma >= bankovka:
                suma -= bankovka
                rozmeneni.append(bankovka)
                print(f"Pouzita bankovka: {bankovka}, zbyva: {suma}")
    else:  # Práce s mincemi
        for mince_hodnota in mince:
            while suma >= mince_hodnota:
                suma -= mince_hodnota
                rozmeneni.append(mince_hodnota)
                print(f"Pouzita mince: {mince_hodnota}, zbyva: {suma}")

print("Rozmeneno:", rozmeneni)
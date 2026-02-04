"""jmeno = input("Zadejte jméno:")
prijmeni = input("Zadejte příjmení:")  
print("Vaše jméno je " + jmeno + " " + prijmeni)"""

"""sirka=int(input("Zadejte šířku:"))
delka=int(input("Zadejte délku:"))
kola=int(input("Zadejte počet kol:"))
jedno_kolo=2*(sirka+delka) 
celkove=jedno_kolo*kola
print("Sirka je " + {sirka} + ", délka je " + {delka} + ", počet kol je " + {kola} + " a celková vzdálenost je " +{celkove}+"m")"""

"""puvodni_cena=input("Zadejte původní cenu zboží:")
sleva=input("Zadejte slevu v %:")
nova_cena=float(puvodni_cena)*(1-float(sleva)/100)
print("Nová cena zboží je " + str(nova_cena) + " Kč")"""

"""teplota=int(input("Zadejte teplotu ve stupních Celsia:"))
if(teplota<=20):
    print("Je zima")
else:
    print("Je teplo")"""

"""cislo=int(input("Zadejte číslo:"))

if cislo<10:
    print("Číslo má jednu cifru")
elif cislo<100:
    print("Číslo má dvě cifry")
elif cislo<1000:
    print("Číslo má tři cifry")
else:
    print("Číslo má více než tři cifry")"""

heslo=str(input("Zadejte heslo:"))
heslo2=str(input("Zadejte heslo znovu:"))
if(heslo.__len__()<8):
    print("Heslo je příliš krátké")
elif(heslo==heslo2):
    print("Heslo je správné")
else:
    print("Heslo je nesprávné")





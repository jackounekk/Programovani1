vys1=0
vstup_1=float(input("Zadej 1.cislo:"))
vstup_2=float(input("Zadej 2.cislo:"))
operace=input("Zadej operaci (+,-,*,/,^,//):")

match operace:
    case "+":
        vys1=vstup_1+vstup_2
    case "-":
        vys1=vstup_1-vstup_2
    case "*":
        vys1=vstup_1*vstup_2
    case "^":
        vys1=vstup_1**vstup_2
    case "//":
        vys1=vstup_1**(1/vstup_2)
    case "/":
        if vstup_2!=0:
            vys1=vstup_1/vstup_2
        else:
            print("Nelze delit nulou")
    case _:
        print("Neplatna operace")

print(f"{vstup_1} {operace} {vstup_2} = {vys1}")
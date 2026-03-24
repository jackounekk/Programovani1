def calculator(a,o,b):
    match o:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if(b==0):
                return "Nelze delit Nulou"
            else:
                return a/b
        case _:
            return "Neplatny operator"
    
a=int(input("Zadejte 1.cislo:"))
o=str(input("Zadejte operator:"))
b=int(input("Zadejte 2.cislo:"))

print(calculator(a,o,b))
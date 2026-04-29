x=int(input("Zadej x:"))
if x<0:
    print("zaporne")
    x=x*-1
    print(f"{x}metru={x*1000}")
elif x>0:
    if x%2==0:
        print("sude")
    else: print("liche")
    print(f"strana:{x}\nobsah:{x*x}\nobvod:{x*4}")
else: print("SES NULA")
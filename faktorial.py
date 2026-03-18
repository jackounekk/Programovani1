
print("Faktorial kalkulacka")
num=int(input("Zadej cislo:"))
fakt=1
for i in range(1,num+1):
    fakt=fakt*i
print(f"{num}!=",int(fakt))
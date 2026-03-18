print("Zjistovac palyndronu")
str=input("Zadejte slovo:")
for i in range (0, str.__len__()):
    if str[i]!=str[str.__len__()-1-i]:
        print("Slovo není palyndrom")
        exit()
print("Slovo je palyndrom")
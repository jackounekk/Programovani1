print("Zjistovac palyndronu")
input=input("Zadejte slovo:")
str= input.lower()
for i in range (0, str.__len__()):
    if str[i]!=str[str.__len__()-1-i]:
        print("Slovo není palyndrom")
        exit()
print("Slovo je palyndrom")
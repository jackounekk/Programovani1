import time 
word=input("Zadejte slovo:")
len=len(word)
for i in range (0,len):
    print(word[i:len])
    for j in range(0,5):
        print(word[i])
        time.sleep(0.5)
        
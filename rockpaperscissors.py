import random
def bot():
    ran=random.randint(1,3)
    match ran:
        case 1:
            return "kamen"
        case 2:
            return "nuzky"
        case 3:
            return "papir"
def winlose(player,bot):
    if(player=="kamen"):
        match bot:
            case "nuzky":
                return "win"
            case "kamen":
                return "draw"
            case "papir":
                return "lose"
    elif(player=="nuzky"):
        match bot:
            case "nuzky":
                return "draw"
            case "kamen":
                return "lose"
            case "papir":
                return "win"
    elif(player=="papir"):
        match bot:
            case "nuzky":
                return "lose"
            case "kamen":
                return "win"
            case "papir":
                return "draw"
    else:
        return "Error"
w=0
d=0
l=0
while True:
    tbot=bot()
    player=str(input("Kamen, nuzky nebo papir?:")).lower().strip()
    print(tbot)
    
    if(winlose(player,tbot)=="win"):
        print("\nwin\n")
        w+=1
    elif(winlose(player,tbot)=="lose"):
        print("\nlose\n")
        l+=1
    elif(winlose(player,tbot)=="draw"):
        print("\ndraw\n")
        d+=1
    else:
        print("Error, neplatny vstup")
    if(w==3):
        print("Konec hry, vyhra!")
        break
    elif(l==3):
        print("\nKonec hry, prohra")
        break

print(f"\nStats:\nWins:{w}\nLost:{l}\nDraws:{d}\nRounds:{w+l+d}")
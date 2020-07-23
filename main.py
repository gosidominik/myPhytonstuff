import random

tomb = ["ko", "papir", "ollo"]

error = False

def Engine(playa, computer):
    if (playa == "ko" and computer == "ko"):
        print("Ko vs. ko. Rematch!")
        print()
    elif (playa == "ko" and computer == "ollo"):
        print("ko vs. ollo. Nyertel!")
        print()
    elif (playa == "ko" and computer == "papir"):
        print("Ko vs. papir. Vesztettel!")
        print()

    elif (playa == "papir" and computer == "ko"):
        print("Papir vs. ko. Nyertel!")
        print()
    elif (playa == "papir" and computer == "ollo"):
        print("Papir vs. ollo. Vesztettel!")
        print()
    elif (playa == "papir" and computer == "papir"):
        print("Papir vs. papir. Rematch!")
        print()

    elif (playa == "ollo" and computer == "ko"):
        print("Ollo vs. ko. Vesztettél!")
        print()
    elif (playa == "ollo" and computer == "ollo"):
        print("Ollo vs. ollo. Rematch!")
        print()
    elif (playa == "ollo" and computer == "papir"):
        print("Ollo vs. papir. Nyertel!")
        print()
    else:
        print("Hibas input!")
        print()
    
def Repaly(rematch):
    rematch = input("Rematch? (y/n) ")
    if (rematch == "n"):
        break
    elif (rematch == "y"):
        continue
    else:
        error = True


while (True):
    playa = input("Ko, papir, ollo!")
    computer = random.randint(0, 2)
    computer = tomb[computer]
    Engine(playa,computer)
    Repaly(rematch)



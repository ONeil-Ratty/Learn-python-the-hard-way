print("You enter a dark room with two. Do you go through door #1 or door #2")

door = input('>')

if door == "1":
    print("There's a giant bear here eatinf a cheese cake, what do you do?")
    print("1. take the cake")
    print("2. Scream at the bear")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job")
    else:
        print(f"Well, doing {bear} is probably better. Bear runs away")
    
elif door == 2:
    print("You star into the endess abyss at Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow Jacket clothespin")
    print("3. understanding revolvers yelling melodies")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by mind of Jello. Good Job!")
    else:
        print("You insanity rots your eyes into a pool of muck. Good Job!")

else:
    print("You stumble around and fall on a knife and die. Good Job!")

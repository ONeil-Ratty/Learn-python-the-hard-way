from entities import Player


class level(object):
    def __init__(self,lvlDiff,numOfenemies):
        self.levelDiff = lvlDiff
        self.numberOfenemies = numOfenemies
        

class start(object):
    def log(self):
        print("what is the name of your character?")
        name = input()
        myPlayer = Player(name,{},[])
        print(f"Welcome to your demise, {name}. Here is a list of starting cats to pick from:\nDobby\nDexter\nLily\n")
        
        firstCat = input()
        if firstCat == "Dobby":
            print("You picked Dobby")
            myPlayer.cats = ["Dobby"]
            return myPlayer
        
        elif firstCat == "Dexter":
            print("You picked Dexter")
            myPlayer.cats = ["Dexter"]
            return myPlayer
        
        elif firstCat == "Lily":
            print("You picked Lily")
            myPlayer.cats = ["Lily"]
            return myPlayer
        else:
            print('You didnt pick a valid cat name')
            return self.log()




        


class EntranceToForrest(level):

    def log(self):
        print("You are a travelor that stumbles upon a the great cat forrest, everything has led to this point " \
        "you will need to overcome it by channeling your ability to talk to cats, befriend, defeat, this is not a mere game" \
        "it is a revelation, a love story about death and cats\n")
        print("you see a great arched door in front of you, with runes around it of an ancient language, you cant decipher it " \
        "what do you do")



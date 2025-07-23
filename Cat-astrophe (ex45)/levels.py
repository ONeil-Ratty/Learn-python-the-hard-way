from entities import Player


class level(object):
    def __init__(self,lvlDiff,numOfenemies):
        self.levelDiff = lvlDiff
        self.numberOfenemies = numOfenemies
        

class start(object):
    def log(self):
        print("what is the name of your character?")
        name = input()
        return name

    def nameOfCharacter(self, name):
        print(f"your name is {name}")



        


class EntranceToForrest(level):

    def log(self):
        print("You are a travelor that stumbles upon a the great cat forrest, everything has led to this point " \
        "you will need to overcome it by channeling your ability to talk to cats, befriend, defeat, this is not a mere game" \
        "it is a revelation, a love story about death and cats\n")
        print("you see a great arched door in front of you, with runes around it of an ancient language, you cant decipher it " \
        "what do you do")



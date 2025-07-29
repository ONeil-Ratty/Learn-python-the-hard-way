from entities import Player


class level(object):
    def __init__(self,lvlDiff,numOfenemies):
        self.levelDiff = lvlDiff
        self.numberOfenemies = numOfenemies
        

class start(object):
    def createPlayer(self):

        # Character name
        print("what is the name of your character?")
        name = input()
        myPlayer = Player(name,{},[])
        print(f"Welcome to your demise, {name}. Here is a list of starting cats to pick from:\nDobby\nDexter\nLily\n")

        # Below is your starter cat 
        firstCat = input()
        if firstCat == "Dobby":
            print("You picked Dobby")
            myPlayer.cats = ["Dobby"]
        
        elif firstCat == "Dexter":
            print("You picked Dexter")
            myPlayer.cats = ["Dexter"]
            
        elif firstCat == "Lily":
            print("You picked Lily")
            myPlayer.cats = ["Lily"]
        
        else:
            print('You didnt pick a valid cat name')
            return self.log()
        
        # below is the first item you get from Character Creation
        print("Choose a starting item to accompany you on your journey: Elixir\nYarn Ball\nCat Treat\n")
        firstItem = input()
        if firstItem == "Elixir":
            myPlayer.items = {"Elixer" : 1}
        elif firstItem == "Yarn Ball":
            myPlayer.items = {"Yarn Ball" : 1}
        elif firstItem == "Cat Treat":
            myPlayer.items = {"Cat Treat" : 1}
        
        return myPlayer
    def next_level(self):
        instantiate = EntranceToForrest()
        return instantiate




        


class EntranceToForrest(object):
    enemies = {"Cat1":10,"Cat2":10}
    playerCatHealth = 10

    def player(self, name, items, cats):
        self.playerName = name
        self.playerItems = items
        self.playerCats = cats  

    def log(self):
        print(f"You are a travelor named that stumbles upon a the great cat forrest, everything has led to this point " \
        "you will need to overcome it by channeling your ability to talk to cats, befriend, defeat, this is not a mere game" \
        "it is a revelation, a love story about death and cats\n")
        print("you see a great arched door in front of you, with runes around it of an ancient language, you cant decipher it " \
        "what do you do")

    while enemies["Cat1"] == 10:
        print("you come accross a wild cat, WHAT DO YOU DO?\n*Fight\n*Item\n*Run")
        action = input()
        if action == "Fight":
            





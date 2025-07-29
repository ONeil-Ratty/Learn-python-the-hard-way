from levels import start
from levels import EntranceToForrest
from entities import Player


started= start()


myPlayer = started.createPlayer()
currentLevel = started.next_level()
currentLevel.log()











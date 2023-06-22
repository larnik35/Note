from interface import mainMenu
from fileManager import *
from counter import Counter

notes = list()
path = "file.csv"
loadFile(notes, Counter.path)
while(mainMenu(notes, Counter.path)):pass

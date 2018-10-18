from CircularPositionalList import CircularPositionalList
from ExternalMethods import ExternalMethods
from ScoreBoard import ScoreBoard

l = CircularPositionalList()
l.append("Archimede")
l.append("Macchia Nera")
l.append("Paperino")
l.append("Pippo")

l1 = CircularPositionalList()
l1.append("Orazio")
l1.append("Gambadilegno")
l1.append("Minni")
l1.append("Pluto")

l1 += l

l2 = CircularPositionalList()

for i in ExternalMethods.bubblesorted(l1):
    l2.append(i)

pos = l2.find("Gambadilegno")
del l2[pos]

print(l2)

scoreboard = ScoreBoard()
new_score = scoreboard.Score("Minni", 1498, "21 Gennaio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Archimede", 2456, "29 Marzo 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Orazio", 11495, "28 Ottobre 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Paperino", 11460, "10 Febbraio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Pippo", 11000, "27 Marzo 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Topolina", 9645, "11 Maggio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Topolino", 1856, "6 Aprile 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Clarabella", 9642, "27 Marzo 2018")
scoreboard.insert(new_score)

scoreboard1 = ScoreBoard()
new_score = scoreboard1.Score("Gambadilegno", 56855, "27 Marzo 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Macchia Gialla", 11, "2 Gennaio 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Macchia Nera", 8887, "2 Gennaio 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Commissario Basettoni", 258962, "27 Marzo 2018")
scoreboard1.insert(new_score)

# print(scoreboard1._sb)

scoreboard.merge(scoreboard1)





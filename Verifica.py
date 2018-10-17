from Progetto1 import CircularPositionalList
from ScoreBoard import ScoreBoard

l = CircularPositionalList()

l.append("Archimede")
l.append("Pippo")
l.append("Macchia Nera")
l.append("Paperino")

tmp = l.bubblesorted()

l1 = CircularPositionalList()
l1.append("Orazio")
l1.append("Gambadilegno")
l1.append("Minni")
l1.append("Pluto")

l3 = tmp.merge(l1.bubblesorted())

l4 = CircularPositionalList()
l4.append("Pippo")
l5 = CircularPositionalList()
l5.append("Pluto")
l5.append("Paolo")
l4 += l5

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
new_score = scoreboard.Score("Gambadilegno", 5655, "27 Marzo 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Macchia Nera", 8887, "2 Gennaio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Commissario Basettoni", 258962, "27 Marzo 2018")
scoreboard.insert(new_score)

# print(scoreboard.top(1))

scoreboard1 = ScoreBoard()
new_score = scoreboard1.Score("Clarabella", 9642, "27 Marzo 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Gambadilegno", 56855, "27 Marzo 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Macchia Nera", 88987, "2 Gennaio 2018")
scoreboard1.insert(new_score)

# print(scoreboard1.top(1))
# print(scoreboard1.last(1))

# l8 = scoreboard._sb.merge(scoreboard._sb)

scoreboard.merge(scoreboard1)
print(scoreboard.top(4))
print(scoreboard.last(8))





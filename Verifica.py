from CircularPositionalList import CircularPositionalList
from ExternalMethods import ExternalMethods
from ScoreBoard import ScoreBoard

l = CircularPositionalList()
l.append("Archimede")
l.append("Pippo")
l.append("Macchia Nera")
l.append("Paperino")

scoreboard = ScoreBoard()
new_score = scoreboard.Score("Minni", 1498, "21 Gennaio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Archimede", 2456, "29 Marzo 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Orazio", 11, "28 Ottobre 2018")
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
new_score = scoreboard.Score("Gambadilegno", 56855, "27 Marzo 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Macchia Gialla", 1, "2 Gennaio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Macchia Nera", 8887, "2 Gennaio 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Commissario Basettoni", 258962, "27 Marzo 2018")
scoreboard.insert(new_score)

scoreboard1 = ScoreBoard()
new_score = scoreboard1.Score("Paolo", 1569, "27 Marzo 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Peppe", 5661, "2 Gennaio 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Antonia", 887, "2 Gennaio 2018")
scoreboard1.insert(new_score)
new_score = scoreboard1.Score("Ciccio", 11125962, "27 Marzo 2018")
scoreboard1.insert(new_score)

scoreboard.merge(scoreboard1)
print(scoreboard._sb)

scoreboard.top(2)








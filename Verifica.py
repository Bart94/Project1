from CircularPositionalList import CircularPositionalList
from ExternalMethods import bubblesorted, merge
from ScoreBoard import ScoreBoard

print("\n----------Inizializzazione CircularPositionalList----------\n")

lista_uno = CircularPositionalList()

print("\nVerifichiamo che inizialmente la lista sia vuota")
print("Esito: {}".format(lista_uno.is_sorted()))

print("\nAggiungiamo gli elementi 4, 10, 6, 9, 15, 8, 0 alla CircularPositionalList lista_uno")
lista_uno.add_last(4)
lista_uno.add_last(10)
lista_uno.add_last(6)
lista_uno.add_last(9)
lista_uno.add_last(15)
lista_uno.add_last(8)
lista_uno.add_last(0)
print(lista_uno)

print("\nAggiungiamo l'elemento 16 in prima posizione")
lista_uno.add_first(16)
print(lista_uno)

print("\nAggiungiamo l'elemento 21 in ultima posizione")
lista_uno.add_last(21)
print(lista_uno)

print("\nAggiungiamo l'elemento 7 prima di 10")
lista_uno.add_before(lista_uno.find(10), 7)
print(lista_uno)

print("\nAggiungiamo l'elemento 32 dopo 15")
lista_uno.add_after(lista_uno.find(15), 32)
print(lista_uno)

print("\nCreiamo una copia della lista_uno chiamata lista_due")
lista_due = lista_uno.copy()
print(lista_due)

print("\nOrdiniamo la nuova lista")
tmp = CircularPositionalList()
for element in bubblesorted(lista_due):
    tmp.add_last(element)
lista_due = tmp
print(lista_due)

print("\nVerifichiamo che la lista sia ordinata")
print("Esito: {}".format(lista_due.is_sorted()))

print("\nStampiamo il primo elemento della nuova lista ordinata")
print(lista_due)
print("Elemento in prima posizione è {}".format(lista_due.first().element()))

print("\nStampiamo l'ultimo elemento della lista ordinata")
print(lista_due)
print("Elemento in ultima posizione è {}".format(lista_due.last().element()))

print("\nStampiamo l'elemento precedente all'elemento in prima posizione")
print(lista_due)
print("Elemento precente a {} è {}".format(lista_due.first().element(), lista_due.before(lista_due.first())))

print("\nStampiamo l'elemento successivo all'elemento in ultima posizione")
print(lista_due)
print("Elemento successivo a {} è {}".format(lista_due.last().element(), lista_due.after(lista_due.last())))

print("\nSostituisco l'elemento 9, se presente, con 28")
lista_due.replace(lista_due.find(9), 28)
print(lista_due)

print("\nVerifichiamo che la lista sia ordinata")
print("Esito: {}".format(lista_due.is_sorted()))

print("\nElimino l'elemento 28")
lista_due.delete(lista_due.find(28))
print(lista_due)

print("\nInverto l'ordine degli elementi nella lista")
lista_due.reverse()
print(lista_due)

print("\nAggiungo 15 in prima posizione e dopo 21")
lista_due.add_first(15)
lista_due.add_after(lista_due.find(21), 15)
print(lista_due)

print("\nConto il numero di occorrenze di 15")
print("Numero di occorrenze {}".format(lista_due.count(15)))

print("\nCreiamo una nuova CircularPositionalList list_tre con i seguenti elementi 24, 2, 15, 16, 18, 3")
lista_tre = CircularPositionalList()
lista_tre.add_last(24)
lista_tre.add_last(2)
lista_tre.add_last(15)
lista_tre.add_last(16)
lista_tre.add_last(18)
lista_tre.add_last(3)

print(lista_tre)

print("\nOrdiniamo la nuova lista")
tmp = CircularPositionalList()
for element in bubblesorted(lista_tre):
    tmp.add_last(element)
lista_tre = tmp
print(lista_tre)

print("\nOrdiniamo lista_due")
tmp = CircularPositionalList()
for element in bubblesorted(lista_due):
    tmp.add_last(element)
lista_due = tmp

print("\nEffettuiamo la merge di lista_due e lista_tre in una nuova lista_quattro")
lista_quattro = merge(lista_due, lista_tre)
print(lista_quattro)

print("\nConto il numero di occorrenze di 15")
print("Numero di occorrenze {}".format(lista_quattro.count(15)))

print("\nRimuovo tutti gli elementi dalla lista invalidando le position")
lista_quattro.clear()
print(lista_quattro)

print("\n----------Inizializzazione Scoreboard----------\n")

print("Scoreboard Uno\n")

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
new_score = scoreboard.Score("Topolino", 1856, "6 Aprile 2018")
scoreboard.insert(new_score)
new_score = scoreboard.Score("Clarabella", 9642, "27 Marzo 2018")
scoreboard.insert(new_score)
print(scoreboard)

print("\nStampo il player con il punteggio più alto in Scoreboard Uno\n")
scoreboard.top()

print("\nStampo i tre player con il punteggio più basso in Scoreboard Uno\n")
scoreboard.last(3)

print("Scoreboard Due\n")
scoreboard_due = ScoreBoard()
new_score = scoreboard_due.Score("Topolina", 9645, "11 Maggio 2018")
scoreboard_due.insert(new_score)
new_score = scoreboard_due.Score("Ciccio", 1125962, "27 Marzo 2018")
scoreboard_due.insert(new_score)
new_score = scoreboard_due.Score("Gambadilegno", 56855, "27 Marzo 2018")
scoreboard_due.insert(new_score)
new_score = scoreboard_due.Score("Macchia Gialla", 1, "2 Gennaio 2018")
scoreboard_due.insert(new_score)
new_score = scoreboard_due.Score("Macchia Nera", 8887, "2 Gennaio 2018")
scoreboard_due.insert(new_score)
new_score = scoreboard_due.Score("Basettoni", 258962, "27 Marzo 2018")
scoreboard_due.insert(new_score)
print(scoreboard_due)

print("\nStampo i 4 player con il punteggio più alto in Scoreboard Due\n")
scoreboard_due.top(4)

print("\nStampo il player con il punteggio più basso in Scoreboard Due\n")
scoreboard_due.last()

print("\nEffettuo la merge dei due scoreboard")
scoreboard.merge(scoreboard_due)
print(scoreboard)

print("\nStampo i 7 player con il punteggio più alto nella nuova Scoreboard\n")
scoreboard.top(7)

print("\nStampo i 5 player con il punteggio più basso nella nuova Scoreboard\n")
scoreboard.last(5)

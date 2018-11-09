from ExternalMethods import *
from CircularPositionalList import CircularPositionalList


class ScoreBoard:
    class Score:
        def __init__(self, player="ComingSoon", score=0, data="NotBorn"):
            self._player = player
            self._score = score
            self._data = data

        def __eq__(self, other):
            return True if self._score == other._score and self._player == other._player else False

        def __le__(self, other):
            if other is None:
                return False
            else:
                return True if self._score <= other._score else False

        def __lt__(self, other):
            if other is None:
                return False
            return True if self._score < other._score else False

        def __gt__(self, other):
            if other is None:
                return True
            else:
                return True if self._score > other._score else False

        def __ge__(self, other):
            if other is None:
                return True
            else:
                return True if self._score >= other._score else False

        def __str__(self):
            return "{:<15}{:<10}{:<25}".format(self._player, self._score, self._data)

    def __init__(self, x=10):
        self._sb = CircularPositionalList()
        self._max_size = x
        self._size = 0

    def __len__(self):
        return self._max_size

    def size(self):
        """ Return the actual number of scores in the scoreboard"""
        return self._size

    def is_empty(self):
        """ Return True if the scoreboard does not contains scores, False at the opposite"""
        return self.size() == 0

    # Caso peggiore O(n)
    def insert(self, s):
        """
            Insert the score s in order if and only if
                - it is not contained in the scoreboard.
                - s is greater than the last score or scoreboard has a free position
            This method does not increment the max size of the scoreboard
        """
        if self._sb.is_empty():
            self._sb.add_first(s)
            self._size += 1
        elif self.size() < self._max_size:
            self._insert_in_order(s)
        elif self._sb.first().element() < s:
            # riduco la size prima di aggiungere un nuovo score
            self._size -= 1
            self._sb.delete(self._sb.first())
            self._insert_in_order(s)

    def _insert_in_order(self, s):
        if s > self._sb.last().element():  # Inserimento in testa
            self._sb.add_last(s)
            self._size += 1
        elif self._sb.find(s) is None:
            one_element_list = CircularPositionalList()
            one_element_list.add_last(s)
            self._sb = merge(self._sb, one_element_list)
            self._size += 1

    def merge(self, new):
        """
            Merge the Scoreboard new with the scoreboard.
            Merging does not affect the order of the scoreboard or the maximum size.
        """
        if type(self) == type(new):
            tmp_ordered_list_score = merge(self._sb, new._sb)
            tmp_ordered_list_score.reverse()

            tmp_new_scoreboard = ScoreBoard(self._max_size)
            for elem in tmp_ordered_list_score:
                tmp_new_scoreboard.insert(elem)
                if tmp_new_scoreboard.size() == self._max_size:
                    break
            self._sb = tmp_new_scoreboard._sb
            self._size = tmp_new_scoreboard._size

    def top(self, i=1):
        """
            Print the the top i scores in the scoreboard.
            Raise an IndexError exception if scoreboard does not contain enough scores to satisfy i.
        """
        tmp = self._sb.copy()
        tmp.reverse()
        cnt = 0
        if i > self.size():
            raise IndexError("Error: not enough values")
        for elem in tmp:
            print(elem)
            cnt += 1
            if cnt == i:
                break

    def last(self, i=1):
        """
            Print the the last i scores in the scoreboard.
            Raise an IndexError exception if scoreboard does not contain enough scores to satisfy i.
        """
        cnt = 0
        if i > self.size():
            raise IndexError("Error: not enough values")
        for elem in self._sb:
            print(elem)
            cnt += 1
            if cnt == i:
                break

    def __str__(self):
        s = ''
        i = 1
        tmp = self._sb.copy()
        tmp.reverse()
        for elem in tmp:
            if elem is not None:
                s += str(i) + '.\t' + str(elem) + '\n'
                i += 1
        for i in range(self._max_size - self._size):
            nope_score = self.Score()
            s += str(self._size + i + 1) + '.\t' + str(nope_score) + '\n'
        s += '-------------------------------------------------------'

        return s

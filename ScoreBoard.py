from CircularPositionalList import CircularPositionalList
from ExternalMethods import ExternalMethods


class ScoreBoard:
    class Score:
        def __init__(self, player="AAAAAAAA", score=0, data="1 Gennaio 1975"):
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
            return self._player + ' ' + str(self._score) + ' ' + self._data

    def __init__(self, x=10):
        self._sb = CircularPositionalList()
        for i in range(x):
            self._sb.append(None)

    def __len__(self):
        return len(self._sb)

    def size(self):
        counter = 0
        current_node = self._sb._header._next
        for i in range(len(self)):
            if current_node._element is not None:
                counter += 1
            current_node = current_node._next
        return counter

    def is_empty(self):
        return True if self.size() == 0 else False

    # Inserisce un nuovo score se e solo se non è peggiore dei risultati già presenti e se
    # la struttura non è piena
    def insert(self, s):
        if self.size() < len(self._sb):
            self._sb.delete(self._sb.last())
            self._sb.add_first(s)
        else:
            min_score = self.getMin()._element
            if min_score is not None and s > min_score:
                self._sb.replace(self._sb.find(min_score), s)

    def _getMin(self):
        current_node = self._sb._header._next
        min = current_node
        if self.size() > 1:
            for i in range(len(self)):
                if current_node._element is not None:
                    if min._element is None:
                        min = current_node
                    elif current_node._element < min._element:
                        min = current_node
                current_node = current_node._next
        return min

    def _getMax(self):
        current_node = self._sb._header._next
        max = current_node
        if self.size() > 1:
            for i in range(len(self)):
                if current_node._element is not None:
                    if max._element is None:
                        max = current_node
                    elif current_node._element > max._element:
                        max = current_node
                current_node = current_node._next
        return max

    def merge(self, new):
        if type(self) == type(new):
            self_copy = CircularPositionalList()
            new_copy = CircularPositionalList()
            lenght = len(self)
            for elem_self in ExternalMethods.bubblesorted(self._sb):
                self_copy.append(elem_self)

            for elem_new in ExternalMethods.bubblesorted(new._sb):
                new_copy.append(elem_new)

            self._sb = ExternalMethods.merge(self_copy, new_copy)
            if self.size() > 10:
                return self.top(10)
            else:
                return self.top(lenght)

    def top(self, i=1):
        """Restituisce i migliori i risultati"""
        temp = CircularPositionalList()
        for elem_new in ExternalMethods.bubblesorted(self._sb):
            temp.append(elem_new)

        self._sb = temp

        if i > self.size():
            raise IndexError("IndexError: no such value with this index")

        if i == 1:
            return self._getMax()._element
        else:
            top = self._getMax()
            j = 0
            l = CircularPositionalList()
            while j < i:
                l.append(top._element)
                top = top._prev
                j += 1
            print(l)

    def last(self, i=1):
        """Restituisce i migliori i risultati"""
        temp = CircularPositionalList()
        for elem_new in ExternalMethods.bubblesorted(self._sb):
            temp.append(elem_new)

        self._sb = temp

        if i > self.size():
            raise IndexError("IndexError: no such value with this index")
        if i == 1:
            return self._getMin()._element
        else:
            top = self._getMin()
            j = 0
            l = CircularPositionalList()
            while j < i:
                l.append(top._element)
                top = top._next
                j += 1
            print(l)

def print_scoreboard(self):
    self._sb.print_element()

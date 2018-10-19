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

    #Caso peggiore O(n)
    def insert(self, s):
        if self.size() == 0:
            self._sb.add_first(s)
            self._sb.delete(self._sb.last())
        else:
            min = self._get_min()
            if s > self._sb._header._next._element:
                self._sb.delete(self._sb.last())
                self._sb.add_first(s)
            elif s < min._element:
                self._insert_in_order(min, s)
            else:
                current_node = self._sb._header._next
                for i in range(self.size() - 1):
                    next_node = current_node._next
                    if current_node._element > s > next_node._element:
                        self._insert_in_order(current_node, s)
                        break
                    current_node = current_node._next

    def _insert_in_order(self, node_one, score):
        self._sb.delete(self._sb.last())
        self._sb.add_after(self._sb.find(node_one._element), score)


    # Inserisce un nuovo score se e solo se non è peggiore dei risultati già presenti e se
    # la struttura non è piena
    # def insert(self, s):
    #     if self.size() < len(self._sb):
    #         self._sb.delete(self._sb.last())
    #         self._sb.add_first(s)
    #     else:
    #         min_score = self._get_min()._element
    #         if min_score is not None and s > min_score:
    #             self._sb.replace(self._sb.find(min_score), s)
    #
    #     if self.size() > 1:
    #         for elem in ExternalMethods.bubblesorted(self._sb):
    #             self._sb.add_first(elem)
    #             self._sb.delete(self._sb.last())

    #Caso peggiore O(n)
    def _get_min(self):
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

    def merge(self, new):
        if type(self) == type(new):
            self_copy = CircularPositionalList()
            new_copy = CircularPositionalList()
            length = len(self)
            for elem_self in ExternalMethods.bubblesorted(self._sb):
                self_copy.append(elem_self)

            for elem_new in ExternalMethods.bubblesorted(new._sb):
                new_copy.append(elem_new)

            self._sb = ExternalMethods.merge(self_copy, new_copy)

            if len(self) > length and len(self) > 10:
                for i in range(len(self) - length):
                    self._sb.delete(self._sb.first())

            self._sb.reverse()


    def top(self, i=1):
        if i > self.size():
            raise IndexError("Error: not enough values")
        elif i == 1:
            print(self._sb.first().element())
        else:
            top = self._sb.first()._node
            for j in range(i):
                print(top._element)
                top = top._next

    def last(self, i=1):
        if i > self.size():
            raise IndexError("IndexError: no such value with this index")
        elif i == 1:
            print(self._get_min()._element)
        else:
            top = self._get_min()
            for j in range(i):
                print(top._element)
                top = top._prev


def print_scoreboard(self):
    self._sb.print_element()

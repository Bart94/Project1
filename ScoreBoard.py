from Progetto1 import CircularPositionalList


class ScoreBoard:
    class Score:
        def __init__(self, player, score, data):
            self._player = player
            self._score = score
            self._data = data

        def __eq__(self, other):
            return True if self._score == other._score else False

        def __le__(self, other):
            return True if self._score <= other._score else False

        def __lt__(self, other):
            if other is None:
                return True
            return True if self._score < other._score else False

        def __gt__(self, other):
            if other is None:
                return True
            else:
                return True if self._score > other._score else False

        def __ge__(self, other):
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
        if self.size() < 1:
            self._sb._header._next._element = s
        elif self.size() < len(self._sb):
            min_score = self.getMin()._element
            if min_score is not None and s > min_score:
                self._sb.delete(self._sb.last())
                self._sb.add_first(s)
        else:
            min_score = self.getMin()._element
            if min_score is not None and s > min_score:
                self._sb.replace(self._sb.find(min_score), s)

    def getMin(self):
        current_node = self._sb._header._next
        min = current_node
        if self.size() > 1:
            for i in range(self.size()):
                if current_node._element is not None and current_node._element < min._element:
                    min = current_node
                current_node = current_node._next
        return min

    def getMax(self):
        current_node = self._sb._header._next
        max = current_node
        if self.size() > 1:
            for i in range(self.size()):
                if current_node._element is not None and current_node._element > max._element:
                    max = current_node
                current_node = current_node._next
        return max

    def merge(self, new):
        if type(self) == type(new):
            self_copy = self._sb.copy()
            new_copy = new._sb.copy()

            if self.size() > 0:
                self_copy = self_copy.bubblesorted()
            if new.size() > 0:
                new_copy = new_copy.bubblesorted()

            size = self.size() + new.size()


            ordered_result = self_copy.bubblesorted()
            ordered_result.reverse()

            temp_scoreboard = ScoreBoard()
            temp_scoreboard._sb = ordered_result
            print(temp_scoreboard.size())

            if (size > 10):
                temp_scoreboard.top(10)
            else:
                temp_scoreboard.top(size)

    def top(self, i=1):
        """Restituisce i migliori i risultati"""
        temp = self._sb.bubblesorted()
        temp.reverse()

        if i > self.size():
            raise IndexError("IndexError: no such value with this index")

        if i == 1:
            return self.getMax()._element
        else:
            top = self.getMax()
            j = 0
            l = CircularPositionalList()
            while j < i:
                l.append(top._element)
                top = top._next
                j += 1
            return l

    def last(self, i=1):
        """Restituisce i migliori i risultati"""
        temp = self._sb.bubblesorted()
        temp.reverse()

        print(temp)

        if i > self.size():
            raise IndexError("IndexError: no such value with this index")
        if i == 1:
            return self.getMin()._element
        else:
            top = self.getMin()
            j = 0
            l = CircularPositionalList()
            while j < i:
                l.append(top._element)
                top = top._prev
                j += 1
            return l


def print_scoreboard(self):
    self._sb.print_element()

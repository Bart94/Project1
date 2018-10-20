from TdP_collections.TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):

    def before(self, p):
        self._validate(p)
        if len(self) == 1:
            return None
        elif p == self.first():
            return self.last().element()
        else:
            return super().before(p).element()

    def after(self, p):
        self._validate(p)
        if len(self) == 1:
            return None
        elif p == self.last():
            return self.first().element()
        else:
            return super().after(p).element()

    def find(self, e):
        front_p = self._header._next
        for i in range(len(self)):
            if front_p._element == e:  # Se il puntatore che scorre in avanti è uguale all'elemento
                return self._make_position(front_p)
            else:
                front_p = front_p._next
        return None

    def is_sorted(self):
        current = self._header._next
        successor = current._next
        if len(self) > 1:
            for i in range(len(self) - 1):
                if current._element <= successor._element:
                    current = current._next
                    successor = current._next
                else:
                    return False
        return True

    def clear(self):
        if self.is_empty():
            return
        else:
            self.delete(self.first())
        return self.clear()

    def count(self, e):
        counter = 0
        for elem in self:
            if e == elem:
                counter += 1
        return counter

    def reverse(self):
        if not self.is_empty():
            current = self._header._next

            for i in range(len(self)):
                current._next, current._prev = current._prev, current._next
                current = current._prev

            self._header._next, self._trailer._prev = self._trailer._prev, self._header._next

    def copy(self):
        copy_list = CircularPositionalList()
        old = self._header._next  # salvo in current il primo elemento della vecchia lista
        for i in range(len(self)):
            copy_list.add_last(old._element)
            old = old._next
        return copy_list

    def __add__(self, other):
        list = self.copy()
        for elem in other:
            list.add_last(elem)
        return list

    def __contains__(self, p):
        try:
            self._validate(p)
            return True
        except:
            return False

    def __getitem__(self, pos):
        return self._validate(pos)._element

    def __len__(self):
        return self._size

    def __setitem__(self, pos, value):
        self._validate(pos)
        self.replace(pos, value)

    def __delitem__(self, pos):
        self._validate(pos)
        self.delete(pos)

    def __iter__(self):
        node = self._header._next
        for i in range(len(self)):
            yield node._element
            node = node._next

    def __str__(self):
        s = '['
        counter = 0
        for elem in self:
            if counter > 0:
                s += ', '
            s += str(elem)
            counter += 1
        s += ']'
        return s

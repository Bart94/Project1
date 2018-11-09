from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):
    """The Circular Positional List is implemented with a Positional List which
        extends a Double Linked List. Each element of the structure is accessible through a position.
        With the methods of this list we access the elements as if they are in a circular list,
        even if it does not reflect its physical implementation.
        """

    # -------------------------- Public Methods --------------------------

    def before(self, p):
        """
        returns the Position of the element before p, None if p has not a predecessor.
        Raise a ValueError if p is not a valid position.

        :param p: Position
        :return: the position of the element before p, None if p has not a predecessor.
        """
        self._validate(p)
        if len(self) == 1:
            return None
        elif p == self.first():
            return self.last().element()
        else:
            return super().before(p).element()

    def after(self, p):
        """
        Returns the Position of the element before p.
        Raise a ValueError if p is not a valid position.

        :param p: Position
        :return: the position of the element after p, None if p has not a successor.
        """
        self._validate(p)
        if len(self) == 1:
            return None
        elif p == self.last():
            return self.first().element()
        else:
            return super().after(p).element()

    def find(self, e):
        """
        Returns the position of the first occurrence of the element e, None if not found.

        :param e: element to find
        :return: The position of the first occurrence of the element e, None if not found.
        """
        front_p = self._header._next
        for i in range(len(self)):
            if front_p._element == e:  # Se il puntatore che scorre in avanti è uguale all'elemento
                return self._make_position(front_p)
            else:
                front_p = front_p._next
        return None

    def is_sorted(self):
        """
        Check if the list is sorted

        :return: True if sorted, else False
        """
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
        """
        Delete each element in the list.

        :return:
        """
        if self.is_empty():
            return
        else:
            self.delete(self.first())
        return self.clear()

    def count(self, e):
        """
        Count the occurrence number of the element e.

        :param e: element to count
        :return: integer with the occurrence number
        """
        counter = 0
        for elem in self:
            if e == elem:
                counter += 1
        return counter

    def reverse(self):
        """
        Reverse the order of the elements in the array

        :return:
        """
        if not self.is_empty():
            current = self._header._next
            old_head, old_tail = self._header._next, self._trailer._prev                        #Conservo i riferimenti alla testa e alla coda

            for i in range(len(self)):
                current._next, current._prev = current._prev, current._next                     #Per ogni nodo scambio i collegamenti 
                current = current._prev

            old_head._next, old_tail._prev = self._trailer, self._header                        #Aggiorno i collegamenti ai puntatori head e trailer
            self._header._next, self._trailer._prev = self._trailer._prev, self._header._next   #Aggiorno i collegamenti dei puntatori alla nuova testa e alla nuova coda

    def copy(self):
        """
        Make a copy of the list and returns it.

        :return: A CircularPositionList equals to the current one.
        """
        copy_list = CircularPositionalList()
        old = self._header._next  
        for i in range(len(self)):
            copy_list.add_last(old._element) 
            old = old._next
        return copy_list

    # -------------------------- Magic Methods --------------------------

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

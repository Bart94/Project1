from TdP_collections.TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):

    def __init__(self, l=None):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._prev = self._trailer
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self._trailer._next = self.header()
        self._size = 0  # number of elements
        if l is not None:
            self._header._next = l._header._next
            self._trailer._prev = l._trailer._prev
            self._size = l._size

    # restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e ValueError
    # se p non è una position della lista

    def before(self, p):
        return super().before(p).element()

    def after(self, p):
        return super().after(p).element()

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        if original is self._header._next:  # Se sto facendo l'inserimento in testa
            return self.add_first(e)
        else:
            return super().add_before(p, e)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        if original is self._trailer._prev:  # Se sto facendo l'inserimento in coda(dopo l'ultimo elemento)
            return self.add_last(e)
        else:
            return super().add_after(p, e)

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        element = node._element
        if node._next == node and node._prev == node:  # se ho un solo elemento collego header e trailer
            self._trailer._prev = self._header
            self._header._next = self._trailer
        elif node == self._header._next:  # elimino in testa su lista non vuota
            self._header._next = node._next  # Cambio il link dell'header al successore
            node._next._prev = self._trailer._prev  # Metto nel prev del nuovo elemento in testa l'elemento in coda
            self._trailer._prev._next = node._next
        elif node == self._trailer._prev:  # elimino in coda
            self._trailer._prev = node._prev  # Cambio il link del trailer al predecessore
            node._prev._next = self._header._next  # Metto nel campo next dell'elemento in coda l'elemento in testa
            self._header._next._prev = node._prev  # Metto nel ccampo prev dell'elemento in test il nuovo elemento in coda
        else:
            node._prev._next = node._next
            node._next._prev = node._prev

        node._next = node._prev = node._element = None
        self._size -= 1
        return element

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def count(self, x):
        counter = 0
        generator = self._generator()
        for elem in generator:
            if x == elem:
                counter += 1
        return counter

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        """ Sovrascrivo il vecchio _insert_between """
        if predecessor is self._header and successor is self._trailer:  # Il primo inserimento in una lista vuota
            newest = self._Node(e, None, None)  # linked to neighbors
            newest._next = newest._prev = newest
            predecessor._next = newest  # Collego il puntatore alla testa e quello alla coda all'elemento
            successor._prev = newest
            self._size += 1
            return self._make_position(newest)
        if predecessor is self._header:  # Inserimento in testa
            new_prec = self._trailer._prev
            newest = self._Node(e, new_prec, successor)  # Collego il nodo alla vecchia testa e alla coda
            successor._prev = newest
            predecessor._next = newest  # Collego il puntatore di testa al nuovo elemento
            new_prec._next = newest  # Collego il next della coda al nuovo elemento in testa
            self._size += 1
            return self._make_position(newest)

        if successor is self._trailer:
            new_succ = self._header._next
            newest = self._Node(e, predecessor, new_succ)  # Collego il nodo al predecessore e al nodo in testa
            predecessor._next = newest
            new_succ._prev = newest
            successor._prev = newest
            self._size += 1
            return self._make_position(newest)

        return super()._insert_between(e, predecessor, successor)

    def find(self, e):
        front_p = self._header._next
        for i in range(0, len(self)):
            if front_p._element == e:  # Se il puntatore che scorre in avanti è uguale all'elemento
                return self._make_position(front_p)
            else:
                front_p = front_p._next
        return None

    def append(self, element):
        self.add_last(element)

    def __len__(self):
        return self._size

    def __getitem__(self, pos):
        return self._validate(pos)._element

    def getNodeByIndex(self, index):
        currentNode = self._header._next

        if index < len(self) and index > -1:
            counter = 0

            while counter < index:
                currentNode = currentNode._next
                counter += 1

            if currentNode is not None:
                return currentNode
            else:
                return None
        else:
            raise IndexError("IndexError: no such value with this index")

    def __setitem__(self, pos, value):
        self._validate(pos)
        self.replace(pos, value)

    def __iadd__(self, other):
        self._trailer._prev._next = other._header._next  # Nel next dell'ultimo elemento(self._trailer._prev) mettici il primo dell'altra lista(other._header._next)
        other._header._next._prev = self._trailer._prev._next
        self._trailer._prev = other._trailer._prev

        self._header._next._prev = self._trailer._prev
        self._trailer._prev._next = self._header._next

        self._size = self._size + other._size
        return self

    def __add__(self, other):
        l = CircularPositionalList(self)
        l += other
        return l

    def __eq__(self, other):
        other_node = other.header()._next
        boolean = True
        if len(self) != len(other):
            return False
        for elem in self:
            if elem == other_node._element:
                other_node = other_node._next
            else:
                return False
        return boolean

    def is_sorted(self):
        current = self._header._next
        successor = current._next
        if len(self) > 1:
            for i in range(len(self) - 1):
                if (current._element is not None and successor._element is not None) and current._element <= successor._element:  # Se il puntatore che scorre in avanti è uguale all'elemento
                    current = current._next
                    successor = current._next
                else:
                    return False
            return True
        else:
            return True

    def reverse(self):
        curr = self._header._next
        for i in range(len(self)):
            curr._next, curr._prev = curr._prev, curr._next
            curr = curr._next
        self._header._next, self._trailer._prev = self._trailer._prev, self._header._next

    # def reverse(self):
    #     first = self._header._next
    #     last = self._trailer._prev
    #     if (len(self) > 1):
    #         counter = 0
    #         while counter < int(len(self) / 2):
    #             first._element, last._element = last._element, first._element
    #
    #             first = first._next
    #             last = last._prev
    #             counter += 1

    def header(self):
        return self._header

    def count(self, x):

        counter = 0
        for elem in self:
            if x == elem:
                counter += 1
        return counter

    def __iter__(self):
        node = self._header._next
        for i in range(len(self)):
            yield node._element
            node = node._next

    def print_element(self):
        generator = self.__iter__()
        for elem in generator:
            print(elem)

    def copy(self):
        copy_list = CircularPositionalList()
        old = self._header._next  # salvo in current il primo elemento della vecchia lista
        counter = 0

        while counter < len(self):
            copy_list.append(old._element)
            old = old._next
            counter += 1

        return copy_list

    def clear(self):
        if self.is_empty():
            return
        else:
            self.delete(self.first())
        return self.clear()

    def pop(self, index=None):
        if index is None:
            index = len(self)

        node = self.getNodeByIndex(index)
        prec = node._prev
        succ = node._next

        prec._next = succ
        succ._prev = prec

        self._size -= 1

        return node._element

    def __contains__(self, p):
        try:
            self._validate(p)
            return True
        except:
            return False

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

    def __delitem__(self, pos):
        self._validate(pos)
        self.delete(pos)

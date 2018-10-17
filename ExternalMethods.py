class ExternalMethods():

    def bubblesorted(self):
        temp = self.copy()
        if not self.is_sorted():
            current_node = temp._header._next
            counter = 0

            if len(self) > 1:
                while counter < (len(temp) - 1):
                    next_node = current_node._next
                    for j in range(counter, len(temp) - 1):
                        if (current_node._element is not None and next_node._element is not None) and current_node._element > next_node._element:
                            current_node._element, next_node._element = next_node._element, current_node._element
                        next_node = next_node._next
                    current_node = current_node._next
                    counter += 1
        return temp

    def merge(self, other):
        if type(self) == type(other):
            if self.is_sorted() and other.is_sorted():
                copy_self = self.copy()
                copy_other = other.copy()
                copy_self += copy_other
                return copy_self.bubblesorted()

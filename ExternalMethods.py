from CircularPositionalList import CircularPositionalList


class ExternalMethods():

    def bubblesorted(cplist):
        temp = cplist.copy()

        if not cplist.is_sorted():
            current_node = temp._header._next

            if len(cplist) > 1:
                for i in range(len(temp) - 1):
                    next_node = current_node._next
                    for j in range(i, len(temp) - 1):
                        if current_node._element is not None or next_node._element is not None:
                            if current_node._element > next_node._element:
                                current_node._element, next_node._element = next_node._element, current_node._element
                        next_node = next_node._next
                    current_node = current_node._next

        for elem in temp:
            yield elem

    def merge(cplist_one, cplist_two):
        ret_list = CircularPositionalList()
        if type(cplist_one) == type(cplist_two):
            if cplist_one.is_sorted() and cplist_two.is_sorted():
                copy_self = cplist_one.copy()
                copy_other = cplist_two.copy()
                copy_self += copy_other
                for elem in ExternalMethods.bubblesorted(copy_self):
                    ret_list.append(elem)
            else:
                raise Exception("Each list must be sorted!")

        return ret_list

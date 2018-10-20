from CircularPositionalList import CircularPositionalList


def bubblesorted(cplist):
    temp = cplist.copy()

    if not cplist.is_sorted():
        current_node = temp._header._next

        for i in range(len(temp) - 1):
            next_node = current_node._next
            for j in range(i, len(temp) - 1):
                if current_node._element is not None or next_node._element is not None:
                    if current_node._element > next_node._element:
                        current_node._element, next_node._element = next_node._element, current_node._element
                next_node = next_node._next
            current_node._element
            current_node = current_node._next

    for elem in temp:
        yield elem


# Caso peggiore O(n)
def merge(cplist_one, cplist_two):
    ret_list = CircularPositionalList()
    if type(cplist_one) == type(cplist_two):
        if cplist_one.is_sorted() and cplist_two.is_sorted():
            if cplist_one.is_empty():
                return cplist_two.copy()
            if cplist_two.is_empty():
                return cplist_one.copy();
            if cplist_one.last().element() > cplist_two.last().element():
                cplist_one, cplist_two = cplist_two, cplist_one
            current = cplist_one._header._next
            current2 = cplist_two._header._next

            for elem in cplist_one:
                while current2._element < elem:
                    ret_list.add_last(current2._element)
                    current2 = current2._next

                current = current._next
                ret_list.add_last(elem)
            while current2._element is not None:
                ret_list.add_last(current2._element)
                current2 = current2._next

        else:
            raise Exception("Each list must be sorted!")
    else:
        raise TypeError("Error in lists type!")
    return ret_list

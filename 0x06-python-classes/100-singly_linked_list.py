#!/usr/bin/python3
class Node:
    """100-linked list"""

    def __init__(self, data, next_node=None):
        """ds"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        return self.__data = value

    @property
    def data(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        return self.__next_node = value


class SinglyLinkedlist:
    """linked"""

    def __init__(self):
        """ds"""
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        add_start = False

        if not self.__head:
            self.__head = new
            new.next_node = None
        else:
            if value < self.__head.data:
                add_start = True
            while tmp.next_node and value > tmp.next_node.data\
                    and not add_start:
                tmp = tmp.next_node
            if not add_start:
                new.next_node = tmp.next_node
                tmp.next_node = new
            else:
                new.next_node = tmp
                self.__head = new
            new.data = value

    def __str__(self):
        s = ""
        current = self.__head

        while current:
            s += str(current.data) + '\n'
            current = current.next_node
        return s[: -1]

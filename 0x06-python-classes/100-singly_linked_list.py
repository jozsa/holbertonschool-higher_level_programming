#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        tmp = self.__head
        ret_str = ""
        while tmp is not None:
            ret_str += str(tmp.data) + '\n'
            tmp = tmp.next_node
        ret_str = ret_str.rstrip()
        return ret_str

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = self.__head
            self.__head = new
        elif self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

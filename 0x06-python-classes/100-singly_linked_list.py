#!/usr/bin/python3
"""
Contains two classes
1. Class Node that defines a node of a singly linked list.
2. Class SinglyLinkedList that defines a singly linked list.
"""


class Node:
    """
    Private instance attributes:
        - __data (int): Data of the node.
        - __next_node (Node): Reference to the next node.

    Instantiation with data and next_node:
        - def __init__(self, data, next_node=None)
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data: The data of the node.
            next_node (Node, optional): Reference to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data with type validation.

        Args:
            value: The value to set as the data.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node with type validation.

        Args:
            value: The value to set as the next_node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Private instance attributes:
        - __head: The head of the linked list.

    Simple instantiation:
        - def __init__(self)
    """
    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (asc).

        Args:
            value: The value to be inserted into the list.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next = self.__head
            self.__head = new_node
        else:
            live = self.__head
            while live.next is not None and live.next.data < value:
                live = live.next
            new_node.next = live.next
            live.next = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        live = self.__head
        while live is not None:
            result += str(live.data) + "\n"
            live = live.next
        return result.strip()


if __name__ == "__main__":
    pass

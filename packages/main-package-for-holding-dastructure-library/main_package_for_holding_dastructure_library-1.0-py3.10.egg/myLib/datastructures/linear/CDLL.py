# Implemntation of CircularDoublyLinkedList

from myLib.datastructures.nodes.DNode import DNode
from .DLL import DoublyLL
import random

class CircularDoublyLL(DoublyLL):

    def __init__(self, node=None):
        super().__init__(node)
        if self.head:
            self.head.prev = self.tail
            self.tail.next = self.head

    def insert_head(self, node):
        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.head = node
        self.tail.next = node
        self.size += 1
        if self.size == 1:
            self.tail = node

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        else:
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
                if (i + 1) > self.size:
                    return
            if current_node == self.tail:
                pass
            node.prev = current_node
            node.next = current_node.next
            current_node.next = node
            node.next.prev = node
            if current_node == self.tail:
                self.tail = node
            self.size += 1

    def sorted_insert(self, new_node):
        if not self.head:
            self.insert_head(new_node)
        else:
            if not self.is_sorted():
                self.sort()

            if new_node.data <= self.head.data:
                self.insert_head(new_node)
            else:
                # unlink head and tail
                self.head.prev = None
                self.tail.next = None

                current_node = self.head
                while current_node.next and current_node.next.data <= new_node.data:
                    current_node = current_node.next
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1

                # relink head and tail
                self.head.prev = self.tail
                self.tail.next = self.head

    def delete_head(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size -= 1

    def sort(self):
        # unlink head and tail
        self.head.prev = None
        self.tail.next = None

        # sort
        super().sort()

        # relink head and tail
        self.head.prev = self.tail
        self.tail.next = self.head

    def is_sorted(self):
        if self.head is None:
            return

        # unlink head and tail
        self.head.prev = None
        self.tail.next = None

        return_value = super().is_sorted()

        # relink head and tail
        self.head.prev = self.tail
        self.tail.next = self.head

        return return_value

    def print(self):
        print("List Size: " ,self.size)
        
        if self.is_sorted():
            print("Sorted Status: Sorted")
        else:
            print("Sorted Status: Not Sorted")
        
        current = self.head
        print("Content List: ", end = " ")
        while self.head is not None:
            print(current.data, end = " ")
            current = current.next
            if current == self.head:
                break
        print("\n")
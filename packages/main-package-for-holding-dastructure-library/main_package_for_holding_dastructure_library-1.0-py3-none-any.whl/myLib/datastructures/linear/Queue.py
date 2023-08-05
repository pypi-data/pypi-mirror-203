# Implemntation of Queue

from .SLL import SLL
from myLib.datastructures.nodes.DNode import DNode


class LLQueue(SLL):

    def __init__(self, head=None):
        super().__init__(head)

    def enqueue(self, node):
        if isinstance(node, int):
            node = DNode(node)
        super().insert_tail(node)

    def dequeue(self):
        return_node = self.head
        super().delete_head()
        return_node.next = None
        return return_node

    def insert_head(self, node):
        return

    def insert_tail(self, node):
        return

    def insert(self, node, position):
        return

    def sorted_insert(self, node):
        return

    def delete_head(self):
        return

    def delete_tail(self):
        return
    
    def delete(self, node):
        return

    def sort(self):
        return
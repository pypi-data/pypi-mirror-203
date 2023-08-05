#Implementation of CircularLinkedList
from myLib.datastructures.linear.SLL import SLL

class CSLL(SLL):
    def __init__(self, head=None):
        super().__init__(head)
        if self.head:
            self.tail.next = self.head

    def insert_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1

    def insert(self, node, position):
        if position < 0 or position > self.size:
            raise IndexError("Index out of range")
        elif position == 0:
            self.insert_head(node)
        elif position == self.size:
            self.insert_tail(node)
        else:
            current = self.head
            for i in range(position-1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def sorted_insert(self, node):
        if (self.size == 0):
            self.insert_head(node)
            return

        current = self.head
        curIndex = 0
        while self.size != curIndex + 1 and self.head is not None:
            if current.data > current.next.data:
                self.sort()
                break
            current = current.next
            curIndex += 1
        
        if not self.head:
            self.head = node
            self.tail = node
            node.next = self.head
        elif node.data < self.head.data:
            self.insert_head(node)
        elif node.data > self.tail.data:
            self.insert_tail(node)
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        
            self.size += 1

    def search(self, node):
        current = self.head
        while current:
            if current.data == node.data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def delete_head(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def delete_tail(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
        self.size -= 1

    def delete(self, node):
        if self.head is None:
            return
        
        current = self.head
        prev = None
        found = False

        while current.next != self.head:
            if current == node:
                found = True
                break
            prev = current
            current = current.next

        if current == node:
            found = True
        
        if found:
            if current == self.head:
                self.head = current.next
                prev = current
                while prev.next != current:
                    prev = prev.next
                prev.next = self.head
            else:
                prev.next = current.next
            self.size -= 1
            if self.size == 0:
                self.head = None
            return
    
    def sort(self):
        if self.size == 1:
            return

        current = self.head.next
        previous = self.head

        sorted = True
        while sorted:
            sorted = False
            while current != self.head:
                if current.data < previous.data:
                    current.data, previous.data = previous.data, current.data
                    sorted = True
                previous = current
                current = current.next
            previous = self.head
            current = self.head.next

    def print(self):
        print("List Size: ", self.size)

        current = self.head
        curIndex = 0
        sorted = True
        while self.size != curIndex + 1 and self.head is not None and self.size != 0:
            if current.data > current.next.data:
                print("Sorted Status: Not Sorted")
                sorted = False
                break
            current = current.next
            curIndex += 1

        if (sorted and self.size != 0):
            print("Sort Status: Sorted")
        
        current = self.head
        curIndex = 0
        print("Content List: ", end = " ")
        while self.size != curIndex:
            print(current.data, end = " ")
            current = current.next
            curIndex += 1
        
        print("\n")

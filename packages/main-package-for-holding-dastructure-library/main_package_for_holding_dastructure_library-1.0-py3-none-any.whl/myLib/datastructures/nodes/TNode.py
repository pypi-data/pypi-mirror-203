class TNode:
    """"A representation of a tree data node for use in various data structures."""
    def __init__(self, data=None, balance=0, parent=None, left=None, right=None):
        self.data = data
        self.balance = balance
        self.parent = parent
        self.left = left
        self.right = right
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
    
    def set_balance(self, balance):
        self.balance = balance
        
    def get_balance(self):
        return self.balance
    
    def set_left(self, left):
        self.left = left
        
    def get_left(self):
        return self.left
    
    def set_right(self, right):
        self.right = right
        
    def get_right(self):
        return self.right
    
    def set_parent(self, parent):
        self.parent = parent
        
    def get_parent(self):
        return self.parent
    
    def print(self):
        print(f"Node value: {self.data}, Balance: {self.balance}")
        
    def __str__(self):
        return str(self.data)
    


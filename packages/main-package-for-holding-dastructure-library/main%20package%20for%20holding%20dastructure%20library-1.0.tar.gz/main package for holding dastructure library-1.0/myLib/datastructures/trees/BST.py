from myLib.datastructures.nodes.TNode import TNode

class BST():
    def __init__(self, root = None):
        if isinstance(root, int):
            root = TNode(root)

        self.root = root
    
    def set_root(self, root):
        if isinstance(root, int):
            root = TNode(root)
            self.root = root
        else:
            self.root = root

    def get_root(self):
        return self.root
    
    def insert(self, data):
        def _insert_node( node):
            if not self.root:
                self.root = node
                return
            current = self.root
            while current:
                if node.data <= current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        break
                elif node.data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        break
        # helper
        def _insert_val( val):
            if not self.root:
                self.root = TNode(val)
                return
            
            
            current = self.root
            while current:
                if val <= current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TNode(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TNode(val)
                        break
        if isinstance(data, int):
            _insert_val(data)
        else:
            _insert_node(data)

    def delete(self, val): 
        def get_min_node(node):
            while node.left:
                node = node.left
            return node
        
        def delete_helper(node, val):
            if not node:
                return node
            elif val < node.data:
                node.left = delete_helper(node.left, val)
            elif val > node.data:
                node.right = delete_helper(node.right, val)
            else:
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    return temp
                temp = get_min_node(node.right)
                node.data = temp.data
                node.right = delete_helper(node.right, temp.data)
            return node
        
        self.root = delete_helper(self.root, val)


    def search(self, val):
        current = self.root
        while current:
            if val == current.data:
                return current
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        
        return None
    
    def print_in_order(self):
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            print(node.data, end = ' ')
            traverse(node.right)
        
        traverse(self.root)
        print()

    def print_bf(self):
        if not self.root:
            return
        
        queue = [self.root]

        while queue:
            curr_level_size = len(queue)

            for i in range(curr_level_size):
                curr = queue.pop(0)
                print(curr.data, end = " ")
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            print()

        print()
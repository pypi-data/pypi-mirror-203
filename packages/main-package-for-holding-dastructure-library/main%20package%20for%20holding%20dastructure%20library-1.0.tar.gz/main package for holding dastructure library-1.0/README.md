# ENSF338-Final-Project

This is the final project for ENSF338 completed by group 42.

This is a python library for data structures that consists of nodes, linear data, and trees.

## Types of Nodes

1. `DNodes` are used to create nodes for the use of the linear data structures. They must be created with an integer. These being Singly Linked List (SLL), Doubly Linked List (DLL), Circular Singly Linked List (CSLL), Circular Doubly Linked List (CDLL), Stack and Queue. Each node will hold the following data members:
    - **data:** Contains an integer value.
    - **next:** Contains the next node, if it doesn't exist then defaults to None.
    - **prev:** Contains the previous node, if it doesn't exist then defaults to None.  
 Example of creating DNode: DNode(10)
    
2. `TNodes` are used to create nodes for the use of trees. These being the Binary Search Tree (BST) and AVL (Self-Balancing Tree). Each node will hold the following data members:
    - **data:** Contains an integer value.
    - **balance:** Contains the height of the tree, used for calculating the balance.
    - **parent:** Contains the node of the parent.
    - **left:** Contains the node to the left.
    - **right:** Contains the node to the right.<br/>
Example of creating TNode: TNode(10)

**Note:** The TNodes also include setters and getters to simulate encapsulation like in java, the user may use the setters and/or getters if they prefer to (As it is optional).

## Types of Linear Structures

1. `Singly Linked List (SLL)`: The data structures may be initialized with nothing, an integer or a node. The methods within an SLL class consist of the following:
    - **insert_head(node):** Inserts a DNode to the head of the linked list.
    - **insert_tail(node):** Inserts a DNode to the tail of the linked list.
    - **insert(node, position):** Inserts a DNode to the specified position. If the position is greater than the size of the linked list, then the DNode is inserted at the tail.
    - **sorted_insert():** Inserts a DNode, if the list is not in order then **sort()** will be called automatically.
    - **delete_head():** Deletes a DNode from the head.
    - **delete_tail():** Deletes a DNode from the tail.
    - **sort():** Sorts the linked list in ascending order
    - **search(node):** Searches for specified node, and returns the node if it exists. Otherwise, None is returned.
    - **clear():** Empties the linked list.
    - **print():** Prints the list size, sorted status and contents within the list.
    - **(Helper) is_sorted()**: Some classes uses the is_sorted(), which users should not need to use themselves, as it only exists to reduce code redundancy.  <br />
Examples of creating Singly Linked List: SLL(), SLL(10), SLL(DNode(10))

2. `Doubly Linked List (DoublyLL)`: Refer to the singly linked list, as all methods and constructors are the same because they are extended from the singly linked list. However, a doubly linked list uses two pointers, one pointing to the next node and the other pointing to the previous node. This means all methods are overridden except search(), clear(), and print() to follow doubly linked list functionality.  <br />
Examples of creating Doubly Linked List: DoublyLL(), DoublyLL(10), DoublyLL(DNode(10))

3. `Circular Singly Linked List (CSLL)`: Refer to the singly linked list, as all methods and constructors are the same because they are extended from the singly linked list. However, a circular singly linked list is connected all around. This means all methods are overridden to follow circular singly linked list functionality. (The changes include using the size to check when to stop)  <br />
Examples of creating Circular Singly Linked List: CSLL(), CSLL(10), CSLL(DNode(10))

4. `CDLL (Circular Doubly Linked List)`: Refer to the singly linked list, as all methods and constructors are the same because they are extended from the singly linked list. However, a circular doubly linked list is connected all around and each node can point to the next and previous node. This means all methods are overridden to follow circular doubly linked list functionality. <br />
Examples of creating Circular Doubly Linked List: CircularDoublyLL(), CircularDoublyLL(10), CircularDoublyLL(DNode(10))

5. `Stack`: The constructors are the same as singly linked list as it has been extended from the singly linked list class. However, the methods are different for the stack. The stack will include these methods:
    - **push(node || int):** Inserts a node into the stack. 
    - **pop():** Deletes the newest node, and returns the deleted node from the stack.
    - **peek():** Look at the top node’s data member.
    - **search(node):** Searches for specified node, and returns the node. Otherwise, return None
    - **clear():** Empties the linked list
    - **print():** Prints the list size, sorted status and contents within the list<br />
Examples of creating a stack: Stack(), Stack(10), Stack(DNode(10))

**IMPORTANT:** As the stack is extended from the SLL class, some methods like insert, delete, and etc. will be unavailable to be used for the stack data structure. As a stack datastructures follows a method of 'First In Last Out' (FILO).

6. `Queue`: The constructors are the same as singly linked list as it has been extended from the singly linked list class. The queue will include these methods:
    - **enqueue(node || int):** Inserts a node into the queue
    - **dequeue():** Deletes the oldest node inserted, and returns the deleted node
    - **search(node):** Searches for specified node, and returns the node. Otherwise, return None
    - **clear():** Empties the linked list
    - **print():** Prints the list size, sorted status and contents within the list<br />
Examples of creating a queue: Queue(), Queue(10), Queue(DNode(10))

**IMPORTANT:** The mentioned methods above are the only methods available for a queue. You may see the other methods, such as insert, delete, sort, and etc. However, they are overwritten to do nothing as a queue follows a method of 'First In First Out' (FIFO)

## Types of Trees

1. `BST (Binary Search Tree)`: The binary search tree can be initialized in three ways, by initializing it with no arguments, an integer, or a TNode. For this implementation, these are the following methods:
    - **set_root(node || int):** Sets a new root, may be used with an integer, node or a tree.
    - **get_root():** Returns the root of the tree
    - **insert(node || int):** Inserts a new node into the tree, if an integer is provided. Then a new node with the integer as data will be created.
    - **delete(int):** Deletes a node given an integer value.
    - **search(int):** Searches for specified integer. Returns the node if found, otherwise, return None.
    - **print_in_order():** Prints the tree in ascending order
    - **print_bf():** Prints the tree in breadth-first search<br />
Examples of creating a binary search tree: BST(), BST(10), BST(TNode(10))

2. `AVL (Self-balancing Tree)`: Refer to the BST (Binary Search Tree), as all methods and constructors are the same because they are extended from the BST. However, AVL is self balancing, so most methods are overridden to allow AVL functionality. The only new method is:
    - **(helper)** **_balance(node):** Not to be used by the user, exists as a helper to reduce redundancy within the code.<br />
Examples of creating an AVL tree: AVL(), AVL(10), AVL(TNode(10))
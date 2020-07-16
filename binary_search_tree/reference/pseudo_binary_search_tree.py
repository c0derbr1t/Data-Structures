"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # Case 1: value is less than self.value
        if value < self.value:
            # IF there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # ELSE repeat the process on left subtree
            else:
                self.left.insert(value)
                # self.left.insert(value)  *RECURSION* we're calling the method from inside itself.

        # Case 2: value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # set max_value to self.value
        # if self.right is None
            # return max_value
        # else
            # return self.right(get_max)
         pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return
        # check if we can move left
        if self.left is not None:
            self.left.in_order_print()

        # visit the node by printing its value
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print()

    """
        ### preorder
        # visit logic
        print(self.value)
        # recurse left
        self.left.fn()
        # recurse right
        self.right.fr()

        ### inorder
        # recurse left
        self.left.fn()
        # visit logic
        print(self.value)
        # recurse right
        self.right.fr()

        ### postorder
        # recurse left
        self.left.fn()
        # recurse right
        self.right.fr()
        # visit logic
        print(self.value)
    """


    # Print the value of every node, starting with the given node,
    # in an **iterative** breadth first traversal
    def bft_print(self, node):
        pass

        # Use a queue to form a "line"
        
        # start by placing the root in the queue

        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
            # dequeue item from front of queue
            # print that item

            # place current item's left node in queue if not None
            # place current iten's right node in queue if not None



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

        # Inititialize an empty stack
        # push the root node onto the stack

        # need a while loop to manage our iteration
        # what do we check in our while statement?

        # while stack is not empty, enter the while loop
            # pop item off the stack
            # print that item's value

            # if there is a right subtree
                # push right item onto the stack
            
            # if there is a left subtree
                # push left item onto the stack

            


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

from singly_linked_list_q import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Implementation with *list*
class Stack_lst:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            popped = None
        else:
            popped = self.storage.pop()
            self.size -= 1
        return popped
        
    # added to try different ways to do stretch in queue.py
    def pop_first(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
        return self.storage[0]

# Implementation with *Linked List*
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

    # added to try different ways to do stretch in queue.py
    def pop_first(self):
        if self.size <= 0:
            return None
        self.size -=1
        return self.storage.remove_head()


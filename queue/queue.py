"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList
from stack import Stack

class Queue_lst:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        
        self.size -= 1
        return self.storage.pop(0)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        
        self.size -= 1
        return self.storage.remove_head()

# ALMOST...
"""
Traceback (most recent call last):
  File "/Users/lambda_school_loaner_252/Desktop/Lambda/CS35/week2/Data-Structures/queue/test_queue.py", line 39, in test_dequeue_respects_order
    self.assertEqual(len(self.q), 0)
AssertionError: 1 != 0
"""
class Queue_stk:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.push(value)

    def dequeue(self):
        if self.size == 0:
            return None

        if self.size == 1:
            return self.storage.pop()

        temp_store = Stack()
        temp = None
        temp_size =  self.size
        if self.size == 2:
            temp = self.storage.pop()
            temp_store.push(temp)
            returned = self.storage.pop()
            self.storage.push(temp)
            self.size -= 1

            return returned

        if self.size > 2:
            while temp_size != 1:
                temp = self.storage.pop()
                temp_store.push(temp)
                temp_size -= 1
                print("hi")
            
            returned = self.storage.pop()
            self.size -= 1
            
            while temp_store.__len__() != 0:
                temp = temp_store.pop()
                self.storage.push(temp)
                print("ABC")

        return returned



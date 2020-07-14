Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
    - O(1) -> because you are always just appending one thing to the end regardless of the data size

2. What is the runtime complexity of `push` using a linked list?
    - O(1) -> still constant, as you are still appending one thing to the end regardless of the data size

3. What is the runtime complexity of `pop` using a list?
    - O(1) --> regardless of the dataset, you are still just taking the last thing off of the list

4. What is the runtime complexity of `pop` using a linked list?
    - O(1) -> If you don't know how it works under the hood it is just removing one thing from the tail of the linked list, no matter the data size.

5. What is the runtime complexity of `len` using a list?
    - O(1) -> It always returns the value stored for self.size. It will not change based on the data size.

6. What is the runtime complexity of `len` using a linked list?
    - O(1) -> Still. It always returns the value stored for self.size. It will not change based on the data size.

## Queue

1. What is the runtime complexity of `enqueue` using a list?
    - O(1) -> You are always just inserting one thing at the beginning, regardless of the data size

2. What is the runtime complexity of `enqueue` using a linked list?
    - O(1) -> Still constant, as you are adding one thing to the tail end of the queue.

3. What is the runtime complexity of `dequeue` using a list?
    - O(1) --> Regardless of the dataset, you are still just taking the last thing off of the queue. It doesn't have to traverse it at all, so size of the data doesn't matter.

4. What is the runtime complexity of `dequeue` using a linked list?
    - O(1) -> If you don't know how it works under the hood it is just removing one thing from the head of the linked list, no matter the data size it will still be the same because you are just doing one thing... remove_head().

5. What is the runtime complexity of `len` using a list?
    - O(1) -> It always returns the value stored for self.size. It will not change based on the data size.

6. What is the runtime complexity of `len` using a linked list?
    - O(1) -> Still. It always returns the value stored for self.size. It will not change based on the data size.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

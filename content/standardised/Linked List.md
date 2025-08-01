---
aliases: 
category: DS
date modified: 27-07-2025
tags:
  - data_structure
  - code_snippet
---
A linked list is a linear data structure in which elements (called nodes) are linked together using pointers. Unlike arrays, linked lists do not store elements in contiguous [[memory]] locations; instead, each node contains:

1. Data – The actual value stored in the node.
2. Pointer (or Reference) – A reference to the next node in the sequence.

### Types of Linked Lists:

1. Singly Linked List – Each node has a pointer to the next node only.
2. Doubly Linked List – Each node has pointers to both the previous and next nodes.
3. Circular Linked List – The last node points back to the first node, forming a circular structure.
    - Circular singly linked list: Last node points to the first node.
    - Circular doubly linked list: Last node points to the first node, and first node points back to the last.

### Advantages of Linked Lists:

- Dynamic size – Unlike arrays, they do not have a fixed size.
- Efficient insertions/deletions – Adding or removing elements does not require shifting (unlike arrays).
- Efficient memory utilization – Memory is allocated as needed.

### Disadvantages of Linked Lists:

- Extra memory usage – Each node requires additional storage for pointers.
- Slower access time – No direct access like arrays; traversal is required.

```python
class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node (initially None)

class LinkedList:
    """A simple singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the list as empty

    def append(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Link the last node to the new node

    def display(self):
        """Print the linked list elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list

    def delete(self, key):
        """Delete a node by value."""
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # If the key was not found
            return

        prev.next = current.next
        current = None

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()  # Output: 10 -> 30 -> None
```
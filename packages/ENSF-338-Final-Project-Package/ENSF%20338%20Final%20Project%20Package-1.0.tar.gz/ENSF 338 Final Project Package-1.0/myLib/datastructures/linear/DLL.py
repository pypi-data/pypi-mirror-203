# Implementation of DoublyLinkedList

import random
from myLib.datastructures.nodes.DNode import DNode
from .SLL import SLL

class DoublyLL(SLL):

    def __init__(self, node=None):
        super().__init__(node)

    def insert_head(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        if self.size == 1:
            self.tail = node

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        else:
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
                if not current_node:
                    return
            node.prev = current_node
            node.next = current_node.next
            current_node.next = node
            if node.next:
                node.next.prev = node
            else:
                self.tail = node
            self.size += 1

    def sorted_insert(self, new_node):
        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            if not self.is_sorted():
                self.sort()

            if new_node.data <= self.head.data:
                new_node.next = self.head
                self.head = new_node
                self.size += 1
            else:
                current_node = self.head
                while current_node.next and current_node.next.data <= new_node.data:
                    current_node = current_node.next
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1

    def delete_head(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def delete(self, node):
        if not node:
            return
        if node == self.head:
            self.delete_head()
        elif node == self.tail:
            self.delete_tail()
        elif self.search(node) is not None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def sort(self):
        # If list is empty or only one element, it is already sorted
        if self.head is None or self.head.next is None:
            return
        
        # Traverse the list starting from the second node
        current_node = self.head.next
        while current_node is not None:
            # Get the value of the current node and save the next node
            current_value = current_node.data
            next_node = current_node.next
            
            # Find the node to insert the current node after
            insert_node = current_node.prev
            while insert_node is not None and insert_node.data > current_value:
                insert_node = insert_node.prev
                
            # If current node is already in the correct position, move to next node
            if insert_node is not None and insert_node.next == current_node:
                current_node = next_node
                continue
            
            # Remove the current node from its current position
            if current_node == self.tail:
                self.tail = current_node.prev
            current_node.prev.next = current_node.next
            if current_node.next is not None:
                current_node.next.prev = current_node.prev
            
            # Insert the current node after the insert node
            current_node.prev = insert_node
            if insert_node is not None:
                current_node.next = insert_node.next
                insert_node.next.prev = current_node
                insert_node.next = current_node
            else:
                current_node.next = self.head
                self.head.prev = current_node
                self.head = current_node
            
            # Move to next node
            current_node = next_node
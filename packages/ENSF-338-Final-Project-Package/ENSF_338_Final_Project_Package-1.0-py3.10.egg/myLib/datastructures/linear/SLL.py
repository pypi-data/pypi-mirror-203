from myLib.datastructures.nodes.DNode import DNode

class SLL:
    def __init__(self, head=None):
        if isinstance(head, int):
            head = DNode(head)
        self.head = head
        self.tail = head
        self.size = 0
        if self.head is not None:
            current = self.head
            while current is not None:
                self.tail = current
                current = current.next
                self.size += 1

    def insert_head(self, node):
        node.next = self.head
        self.head = node
        self.size += 1
        if self.size == 1:
            self.tail = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position == 0:
            self.InsertHead(node)
            return
        current = self.head
        prev = None
        pos = 0

        while current is not None and pos < position:
            prev = current
            current = current.next
            pos += 1
        prev.next = node
        node.next = current
        self.size+= 1

    def sorted_insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1

        else:
            current = self.head
            # sorts the linkedlist if not already sorted
            while current is not None and current.next is not None:
                if current.data > current.next.data:
                    self.sort()
                    break
                current = current.next
            
            if node.data < self.head.data:
                self.insert_head(node)
            elif node.data > self.tail.data:
                self.insert_tail(node)
            else:
                current = self.head
                while current.next is not None and node.data > current.next.data:
                    current = current.next
                node.next = current.next

                current.next = node
                self.size += 1

    def search(self, node):
        current_node = self.head
        while current_node:
            if current_node.data == node.data:
                return current_node
            current_node = current_node.next
        return None

    def delete_head(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1
        if not self.head:
            self.tail = None

    def delete_tail(self):
        if not self.head:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.size -= 1

    def delete(self, node):
        if not self.head:
            return
        if self.head.data == node.data:
            self.delete_head()
            return
        current_node = self.head.next
        prev_node = self.head
        while current_node:
            if current_node.data == node.data:
                prev_node.next = current_node.next
                self.size -= 1
                if current_node == self.tail:
                    self.tail = prev_node
                return
            prev_node = current_node
            current_node = current_node.next

    def sort(self):
        if not self.head or not self.head.next:
            return
    
        sorted_list = None
        current = self.head
        while current:
            node = current
            current = current.next

            if not sorted_list or node.data <= sorted_list.data:
                node.next = sorted_list
                sorted_list = node
            else:
                current_sorted = sorted_list
                while current_sorted.next and current_sorted.next.data < node.data:
                    current_sorted = current_sorted.next

                node.next = current_sorted.next
                current_sorted.next = node
            self.head = sorted_list
            while self.tail.next:
                self.tail = self.tail.next
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        print("List Size: " ,self.size)
        
        if self.is_sorted():
            print("Sorted Status: Sorted")
        else:
            print("Sorted Status: Not Sorted")
        
        current = self.head
        print("Content List: ", end = " ")
        while current is not None:
            print(current.data, end = " ")
            current = current.next
        print("\n")
        
    def is_sorted(self):
            if not self.head or not self.head.next:
                return True

            current_node = self.head
            while current_node.next:
                if current_node.data > current_node.next.data:
                    return False
                current_node = current_node.next

            return True
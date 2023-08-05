from myLib.datastructures.linear.singlyLL import SinglyLinkedList


class CircularSinglyLinkedList(SinglyLinkedList):
    def __init__(self, node=None):
        super().__init__()
        if node:
            self.head = node
            node.next = node
            self.tail = node
            self.length = 1
    
    def insert_head(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node
        self.length += 1
    
    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def DeleteHead(self):
        if self.head is None:
            return
        elif self.head.next == self.head:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            value = self.head.value
            self.tail.next = self.head.next
            self.head = self.head.next
            self.length -= 1
            return value
    
    def DeleteTail(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            value = self.tail.value
            current_node.next = self.head
            self.tail = current_node
            self.length -= 1
            return value
    
    def Print(self):
        """Prints the list information on the screen."""
        print("List length:", self.length)
        print("List content:")
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break

from myLib.datastructures.nodes import DNode


from myLib.datastructures.linear.doublyLL import DoublyLinkedList



class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        if self.head is not None:
            self.head.previous = self.tail
        if self.tail is not None:
            self.tail.next = self.head

    def insert_head(self, node):
        super().insert_head(node)
        if self.head.next is not None:
            self.head.next.previous = self.head
        self.head.previous = self.tail
        self.tail.next = self.head

    def insert_tail(self, node):
        if self.tail is None:
            super().insert_head(node)
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            self.head.previous = self.tail
            self.length += 1

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        elif position >= self.length:
            self.insert_tail(node)
        else:
            curr = self.head
            for i in range(position-1):
                curr = curr.next
            node.next = curr.next
            node.previous = curr
            curr.next.previous = node
            curr.next = node
            self.length += 1

    def DeleteHead(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.tail = None
        else:
            self.head.next.previous = None
        self.head = self.head.next
        self.head.previous = self.tail
        self.tail.next = self.head
        self.length -= 1


    def DeleteTail(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.value
            self.tail.previous.next = None
            self.tail = self.tail.previous
            self.tail.next = self.head
            self.head.previous = self.tail
            self.length -= 1
            return value

    def Delete(self, node):
        if self.head == None:
            return None
        elif self.head == node:
            self.head = node.next
            if self.head is not None:
                self.head.previous = self.tail
                self.tail.next = self.head
            return node.value
        elif self.tail == node:
            self.tail = node.previous
            self.tail.next = self.head
            self.head.previous = self.tail
            return node.value
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            return node.value

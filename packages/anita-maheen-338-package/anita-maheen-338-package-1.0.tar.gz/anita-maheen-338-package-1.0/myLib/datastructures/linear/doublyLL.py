from myLib.datastructures.linear.singlyLL import SinglyLinkedList

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def insert_head(self, node):
        super().insert_head(node)
        if self.head.next is not None:
            self.head.next.previous = self.head

    def insert_tail(self, node):
        if self.tail is None:
            super().insert_head(node)
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
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
            return
        if self.head.next is None:
            self.tail = None
        else:
            self.head.next.previous = None
        self.head = self.head.next
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
            self.length -= 1
            return value

    def Delete(self, node):
        if self.head == None:
            return None
        elif self.head == node:
            self.head = node.next
            if self.head is not None:
                self.head.previous = None
            return node.value
        elif self.tail == node:
            self.tail = node.previous
            self.tail.next = None
            return node.value
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            return node.value

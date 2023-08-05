from myLib.datastructures.linear.singlyLL import SinglyLinkedList

class Stack(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def push(self, node):
        self.insert_head(node)

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.value

    def peek(self):
        if self.head is None:
            return None

        return self.head.value

    def is_empty(self):
        return self.head is None

    # overriding the InsertTail method with empty body
    def insert_tail(self, node):
        pass

    # overriding the insert method with empty body
    def insert(self, node, position):
        pass

    # overriding the SortedInsert method with empty body
    def SortedInsert(self, node):
        pass

    # overriding the DeleteHead method with empty body
    def DeleteHead(self):
        pass

    # overriding the DeleteTail method with empty body
    def DeleteTail(self):
        pass

    # overriding the Delete method with empty body
    def Delete(self, node):
        pass

    # overriding the Sort method with empty body
    def Sort(self):
        pass

    # overriding the Print method with empty body
    def Print(self):
        pass

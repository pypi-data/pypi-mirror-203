class DNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
        self.next = None
        self.head = None
        self.tail = None
        self.sorted = True
        self.length = 0
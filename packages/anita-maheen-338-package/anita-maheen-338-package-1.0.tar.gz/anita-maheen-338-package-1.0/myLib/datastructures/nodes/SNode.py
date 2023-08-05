class SNode:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.sorted = True
        self.length = 0
        self.value = value
        self.next = None
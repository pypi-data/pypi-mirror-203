from myLib.datastructures.linear.singlyLL import SinglyLinkedList


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, node):
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.value

    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.value

        
    # Override methods that are not applicable to queue with empty body methods
    def SortedInsert(self, node):
        pass
    
    def isSorted(self):
        pass
    
    def Search(self, value):
        pass
    
    def DeleteHead(self):
        pass
    
    def DeleteTail(self):
        pass
    
    def Delete(self, node):
        pass

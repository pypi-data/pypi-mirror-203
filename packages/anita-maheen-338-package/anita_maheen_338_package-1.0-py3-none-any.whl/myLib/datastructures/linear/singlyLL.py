
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sorted = True
        self.length = 0
        
        
    def insert_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.sorted = True
        else:
            node.next = self.head
            self.head = node
            self.sorted = False


    
    def insert_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        self.sorted = False

    def insert(self, node, position):
        if position < 0:
            raise ValueError("Position must be non-negative")

        if position == 0:
            self.insert_head(node)
        else:
            curr = self.head
            for i in range(position - 1):
                if curr is None:
                    raise ValueError("Position is out of range")
                curr = curr.next

            if curr is None:
                raise ValueError("Position is out of range")

            node.next = curr.next
            curr.next = node
            if node.next is None:
                self.tail = node

        self.length += 1


    def SortedInsert(self, node):
        if self.head is None:
            self.insert_head(node)
            return

        if not self.sorted:
            self.Sort()

        current = self.head
        prev = None
        while current is not None and current.value < node.value:
            prev = current
            current = current.next

        if prev is None:
            self.insert_head(node)
        else:
            node.next = current
            prev.next = node

        self.length += 1
        self.sorted = self.isSorted()


    
    def isSorted(self):
        current = self.head
        is_sorted = True
        while current is not None and current.next is not None:
            if current.value > current.next.value:
                is_sorted = False
            current = current.next
        return is_sorted

    def Search(self, value):
        current = self.head
        while current is not None:
            if current.value == value: # Change `data` to `value`
                return current
            current = current.next
        return None



    def DeleteHead(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
    


    
    def DeleteTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current
        self.length -= 1




    
    def Delete(self, node):
        if self.head is None:
            return None
        elif self.head == node:
            self.head = node.next
            if self.tail == node:
                self.tail = None
            self.length -= 1
            return node.value
        else:
            current_node = self.head
            while current_node is not None and current_node.next != node:
                current_node = current_node.next
            if current_node is None:
                return None
            else:
                current_node.next = node.next
            if self.tail == node:
                self.tail = current_node
            self.length -= 1
            return node.value
        
    def Sort(self):
        if self.head is None:
            return
        
        current = self.head
        while current is not None:
            min_node = current
            runner = current.next
            while runner is not None:
                if runner.value < min_node.value:
                    min_node = runner
                runner = runner.next
            
            if min_node != current:
                current.value, min_node.value = min_node.value, current.value
            
            current = current.next
        
        self.sorted = True



    def Clear(self):
        """Deletes the whole list."""
        self.head = None
        self.tail = None
        self.sorted = True
        self.length = 0

    def Print(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" -> ")
                current = current.next
            print("None")


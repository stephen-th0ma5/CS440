class Frontier:
    head = None
    size = 0

    def push(self, node):
        self.size += 1
        if(self.head is None):
            self.head = node
        else:
            node.next= self.head
            self.head = node

    def pop(self):
        self.size -= 1
        if(self.head is None):
            return None
        elif(self.head.next is None):
            self.head = None
            return self.head
        self.head = self.head.next
        return self.head

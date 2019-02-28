class Frontier:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, node):
        self.size += 1
        if(self.head is None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        self.size -= 1
        if(self.head is None):
            return None
        elif(self.head.next is None):
            node = self.head
            self.head = None
            return node
        node = self.head
        self.head = self.head.next
        return node

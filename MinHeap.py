import math

class MinHeap:

    def __init__(self):
        self.size = 0
        self.arr = []

    def insert(self, node):
        self.size += 1
        self.arr.append(node)
        self.sift_up(len(self.arr) - 1)

    def get(self, target):
        for node in self.arr:
            if(node == target):
                return node.f_value
        #returns -1 if node doesn't exist
        return -1

    def peek(self):
        if(self.size == 0):
            return None
        return self.arr[0].f_value

    def delete(self, target):
        index = self.arr.index(target)
        if(index == self.size - 1):
            self.arr.pop()
            self.size -= 1
        elif(index == 0):
            self.pop()
        else:
            self.arr[index] = self.arr[self.size - 1]
            self.arr.pop()
            self.size -= 1
            if(self.arr[index].f_value < self.arr[math.floor(index/2)].f_value):
                self.sift_up(index)
            else:
                self.sift_down(index)


    def sift_up(self, index):
        i = index
        while(i != 0):
            parent = math.floor(i / 2)
            if(self.arr[i].f_value <= self.arr[parent].f_value):
                temp = self.arr[i]
                self.arr[i] = self.arr[parent]
                self.arr[parent] = temp
                i = parent
            else:
                break

    def pop(self):
        if(self.size == 0):
            return None
        self.size -= 1
        result = self.arr[0]
        end_index = len(self.arr) - 1
        self.arr[0] = self.arr[end_index]
        self.arr.pop()
        self.sift_down(0)
        return result

    def sift_down(self, index):
        parent = index
        left_child = index + 1
        right_child = index + 2
        if(right_child >= self.size and left_child >= self.size):
            #no right or left child
            return
        elif(right_child >= self.size):
            #no right child
            temp = self.arr[parent]
            self.arr[parent] = self.arr[left_child]
            self.arr[left_child] = temp
            return
        while(parent < self.size and (self.arr[parent].f_value > self.arr[left_child].f_value or self.arr[parent].f_value > self.arr[right_child].f_value)):
            if(self.arr[left_child].f_value < self.arr[right_child].f_value):
                temp = self.arr[parent]
                self.arr[parent] = self.arr[left_child]
                self.arr[left_child] = temp
                parent = left_child
            elif(self.arr[left_child].f_value == self.arr[right_child].f_value):
                if(self.arr[left_child].g_value < self.arr[right_child].g_value):
                    temp = self.arr[parent]
                    self.arr[parent] = self.arr[left_child]
                    self.arr[left_child] = temp
                    parent = left_child
                else:
                    temp = self.arr[parent]
                    self.arr[parent] = self.arr[right_child]
                    self.arr[right_child] = temp
                    parent = right_child
            else:
                temp = self.arr[parent]
                self.arr[parent] = self.arr[right_child]
                self.arr[right_child] = temp
                parent = right_child
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2
            if(left_child >= self.size or right_child >= self.size):
                break;


    def traverse(self):
        for item in self.arr:
            print(item.f_value)

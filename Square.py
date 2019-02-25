
class Square:

    def __init__(self, value, x, y):
        self.value = value
        self.children = []
        self.value = 0
        self.x = x
        self.y = y
        self.visited = False
        self.blocked = False
        self.startBlock = False
        self.endBlock = False
        self.g_value = 0
        self.h_value = 0
        self.f_value = self.g_value + self.h_value
        self.parent = None
        self.search_value = 0


class Square:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.value = 0
        self.visited = False
        self.blocked = False
        self.g_value = 0
        self.h_value = 0
        self.f_value = self.g_value + self.h_value
        self.tree_pointer = None
        self.search_value = 0

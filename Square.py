class Square:
    value = 0
    visited = False
    blocked = False
    g_value = 0
    h_value = 0
    f_value = g_value + h_value
    tree_pointer = None
    search_value = 0
    children = []

    def __init__(self, value):
        self.value = value

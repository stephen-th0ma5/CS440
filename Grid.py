from Square import Square

class Grid:

    def __init__(self):
        self.environment = [[None] * 101 for _ in range(101)]

    def print_grid(self):
        for i in range(101):
            for j in range(101):
                print(self.environment[i][j])
            print("")

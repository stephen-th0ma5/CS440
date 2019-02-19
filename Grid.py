from Square import Square

class Grid:
    environment = []

    def __init__(self):
        for i in range(101):
            self.environment.append([])
            for j in range(101):
                self.environment[i].append(Square(0))
                tuple = ("North", Square(0))
                arr.append(tuple)

    def print_grid(self):
        for i in range(101):
            for j in range(101):
                print(self.environment[i][j].value, end=' ')
            print("")

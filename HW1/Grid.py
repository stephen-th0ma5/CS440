from Square import Square
from settings import *

class Grid:

    def __init__(self):
        self.environment = [[None] * DIM for _ in range(DIM)]

import random
import math

# Constants
BOARD_SIZE = 20 # Board size (rows * columns)
TURN_CHANGE = 5 # How many cells the snakes move at once
CELL_WIDTH = 10 # Width of one cell on screen
CELL_HEIGHT = 10 # Height of one cell on screen
FOOD_RADIUS = 3 # Radius of food (sqrt(2)/2 because circle on Cartesian plane)
MAX_LENGTH = 7 # Maximum length of snakes (number of segments/cells per snake)
POWERUP_MULTIPLIER = 4 # Multiplier applied to turn change when eating powerup
FINISHED_MESSAGE = 'You have finished the Snake Game!'

class Cell:
    def __init__(self, row=0, col=0):
        self._row = row # Row index (0 based)
        self._col = col # Column index (0 based)
        
    @property
    def position(self):
        return f'({self._row}, {self._col})' # Format position as string for display
    
    def empty(self):
        pass # Implement me! Check if cell contains nothing (i.e., no snake or food)
    
    def occupiedByHead(self, snake):
        headIndex = snake._head_index()
        nextCellIndex = headIndex + TURN_CHANGE
        # Check if head segment is adjacent and aligned with this cell
        if abs(nextCellIndex - self._col) == 1 and abs(nextCellIndex - self._row) == 1:
            xDiff = int((self._col - nextCellIndex) / CELL_WIDTH)
            yDiff = int((self._row - nextCellIndex) / CELL_WIDTH)
            return True
        else:
            return False

class Food:
    def __init__(self, pos=None):
        self._pos = pos # Optional: Pass None for random placement during generation loop
        
    @property
    def center(self):
        halfWidth = CELL_WIDTH // 2 # Half width of food square (assume centered within cell)
        return tuple([int(math.floor(halfWidth)) for _ in range(2)]) # Coordinates of food center

    def checkForCollisionWithSelf(self):
        radius = FOOD_RADIUS # Diameter of food (sqrt(2), but rounded down to integer due to flooring later)
        halfWidth = CELL_WIDTH // 2 # Half width of cell
        halfHeight = CELL_HEIGHT // 2 # Half height o
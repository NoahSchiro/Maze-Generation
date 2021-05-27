import pygame
import math

# Constants for pygame
WIDTH, HEIGHT = 500, 500
BLACK = 0,0,0
WHITE = 255,255,255
LIGHT_BLUE = 6,15,140
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
FPS = 30
clock = pygame.time.Clock()

#Cell constants
cell_width = 50
line_width = 2
cols, rows = math.floor(WIDTH / cell_width), math.floor(HEIGHT / cell_width)

#Cell class is each tile of our maze
class Cell:

    def __init__(self, x, y):
        self.x = x  #Col number
        self.y = y  #Row Number

        #Positions based on pixels
        self.x_pos = x * cell_width
        self.y_pos = y * cell_width


        #Determines whether or not to draw the respective line
        self.top_line    = True
        self.right_line  = True
        self.bottom_line = True
        self.left_line   = True

        #Keeps track of whether or not the 
        #cell has been visited for the backtracking algorithm
        self.visited = False
    
    #Method for drawing the cell
    def draw(self):
        
        #Colors cell if it was already visited
        if self.visited:
            pygame.draw.rect(WIN, LIGHT_BLUE, (self.x_pos, self.y_pos, cell_width, cell_width))
        
        #Draws the walls of each cell
        if self.top_line:
            pygame.draw.line(WIN, WHITE, (self.x_pos, self.y_pos), (self.x_pos+cell_width, self.y_pos), line_width)
        if self.right_line:
            pygame.draw.line(WIN, WHITE, (self.x_pos+cell_width, self.y_pos), (self.x_pos+cell_width, self.y_pos+cell_width), line_width)
        if self.bottom_line:
            pygame.draw.line(WIN, WHITE, (self.x_pos+cell_width, self.y_pos+cell_width), (self.x_pos, self.y_pos+cell_width), line_width)
        if self.left_line:
            pygame.draw.line(WIN, WHITE, (self.x_pos, self.y_pos+cell_width), (self.x_pos, self.y_pos), line_width)

        
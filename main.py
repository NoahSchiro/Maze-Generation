from cell import *
import random
pygame.init()

# Set up
grid = []                       #Maze grid
for y in range(rows):
    temp_row = []               #Temporary row
    for x  in range(cols):
        temp = Cell(x,y)        #Create cells in that row
        temp_row.append(temp)   #Put them in that row
    
    grid.append(temp_row)       #Put row in grid

#For any given cell, returns a random neighboring cell
def get_random_neighbor(cell):

    #Create a list to store possible choices
    neighbors = []

    #Loop through grid to find the input cell
    for y in range(rows):
        for x in range(cols):
            
            #Once we have found the cell
            if cell.y == y and cell.x == x:
                
                #Top neighbor
                if y-1 >= 0 and not grid[y-1][x].visited:
                    neighbors.append(grid[y-1] [x])
                #Right neighbor
                if x+1 <= cols-1 and not grid[y][x+1].visited:
                    neighbors.append(grid[y] [x+1])
                #Bottom neighbor
                if y+1 <= rows-1 and not grid[y+1][x].visited:
                    neighbors.append(grid[y+1] [x])
                #Left neighbor
                if x-1 >= 0 and not grid[y][x-1].visited:
                    neighbors.append(grid[y] [x-1])

    #If there are potential neighbors
    if len(neighbors) > 0:
        
        #Randomly select one
        random_index = random.randint(0, len(neighbors)-1)
        return neighbors[random_index]

#Removes the walls from one cell to another
def remove_walls(current, next):

    delta_x = current.x - next.x
    delta_y = current.y - next.y

    if delta_x == -1:

        current.right_line = False
        next.left_line = False
    
    elif delta_x == 1:
        
        current.left_line = False
        next.right_line = False

    elif delta_y == -1:
        
        current.bottom_line = False
        next.top_line = False

    elif delta_y == 1:
        
        current.top_line = False
        next.bottom_line = False

#Stack for the backtracking part of the algo
stack = []

#Sets the starting point in the top right corner
current_cell = grid[0][0]

maze_complete = False

#Main loop
while 1:

    clock.tick(FPS)

    # Checks to see if user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if not maze_complete:
        #Mark current cell as visited
        current_cell.visited = True

        next_cell = get_random_neighbor(current_cell)
        
        #Checks to make sure we actually have a valid neighbor
        if next_cell:

            #Add the cell to the stack
            stack.append(current_cell)

            #Remove walls between current_cell and next_cell, 
            #then let the next_cell become the next current_cell
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        
        #If no valid neighbor, backtrack
        elif len(stack) > 0:
            current_cell = stack.pop()
        
        #When stack empties, maze is complete
        elif len(stack) == 0 and not next_cell:
            maze_complete = True

        #Draw all cells
        for y in range(rows):
            for x in range(cols):
                grid[y][x].draw()
    
    else:
        print("Maze complete!")

    pygame.display.update()
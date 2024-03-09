import pygame
import numpy as np
import sys

# # Initialize Pygame
# pygame.init()

# # Set up display
# CELL_SIZE = 10
# GRID_WIDTH, GRID_HEIGHT = 80, 60
# WIDTH, HEIGHT = GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Matrix-style Falling Sand Game")

# # Define colors
# WHITE = (255, 255, 255)


height=10
width=10

def display_array(array):
    pygame.init()
    screen_width = 300
    screen_height = 300

    height = screen_height // 10
    width = screen_width // 10

    array = make_2d_arr(height, width)

    cell_size = min(screen_width // (width + 1), screen_height // (height + 1))+5
    margin = 0

    screen_width = (cell_size + margin) * width + margin
    screen_height = (cell_size + margin) * height + margin

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    
    is_dragging = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                clicked_row = mouse_pos[1] // (cell_size + margin)
                clicked_col = mouse_pos[0] // (cell_size + margin)
                array[clicked_row][clicked_col] = 1

        screen.fill((255, 255, 255))

        for row in range(len(array)):
            for col in range(len(array[0])):
                color = (0, 0, 0) if array[row][col] == 0 else (255, 0, 0)
                pygame.draw.rect(screen, color, (col * (cell_size + margin), row * (cell_size + margin), cell_size, cell_size))
                
                
        #xyz
                
        for row in range(len(array) - 1, -1, -1):  # iterate from bottom to top
            for col in range(len(array[row])):
                if array[row][col] == 1 and row < len(array) - 1 and array[row + 1][col] == 0:
                    array[row + 1][col] = 1
                    array[row][col] = 0


        pygame.display.flip()
        clock.tick(30)
        














def make_2d_arr(height, width):
    
    x=[]
    
    for i in range(0,height):
        lst=[]
        
        for j in range(0,width):
            lst.append(0)
        x.append(lst)
        
    return x

    pass


arr=make_2d_arr(height, width)

def print_2d():
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            print(arr[i][j],end="")
        print()
        
        
        
        

    


# ch=True

# print_2d()

# while(ch):
    
#     x=int(input())
#     y=int(input())
    
#     arr[x][y]=1
    
#     print_2d()
    
    
display_array(arr)



# Main game loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()

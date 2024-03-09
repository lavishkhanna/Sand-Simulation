import pygame
import numpy as np
import sys
import random
import math

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

def interpolate_color(color1, color2, t):
    """
    Interpolates between two colors color1 and color2.
    t should be a value between 0 and 1 indicating the interpolation factor.
    """
    r = int(color1[0] * (1 - t) + color2[0] * t)
    g = int(color1[1] * (1 - t) + color2[1] * t)
    b = int(color1[2] * (1 - t) + color2[2] * t)
    return (r, g, b)


height=10
width=10

def display_array(array):
    pygame.init()
    screen_width = 800
    screen_height = 800

    height = screen_height // 10
    width = screen_width // 10

    array = make_2d_arr(height, width)

    cell_size = min(screen_width // (width + 1), screen_height // (height + 1))
    margin = 0

    screen_width = (cell_size + margin) * width + margin
    screen_height = (cell_size + margin) * height + margin

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    
    is_dragging = False
    
    num_particles=5
    
    cnt=204
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                clicked_row = mouse_pos[1] // (cell_size + margin)
                clicked_col = mouse_pos[0] // (cell_size + margin)

                for _ in range(num_particles):
                # Ensure particles stay within array bounds
                    particle_row = clicked_row + random.randint(-2, 2)
                    particle_col = clicked_col + random.randint(-2, 2)

                    if 0 <= particle_row < len(array) and 0 <= particle_col < len(array[0]):
                        array[particle_row][particle_col] = 1
                
                
                

        screen.fill((169, 169, 169))
        
        

        for row in range(len(array)):
            for col in range(len(array[0])):
                color = (0, 0, 0) if array[row][col] == 0 else (236, 204, 162)
                
                pygame.draw.rect(screen, color, (col * (cell_size + margin), row * (cell_size + margin), cell_size, cell_size))
                
                
        #xyz
        cnt=cnt+1
        
        if(cnt>=255):
            cnt=204
                
        for row in range(len(array) - 1, -1, -1):  # iterate from bottom to top
            for col in range(len(array[row])):
                
                if array[row][col] == 1:
                    color = (0, 0, 0) if array[row][col] == 0 else (236, cnt, 162)
                
                if array[row][col] == 1 and row < len(array) - 1 and array[row + 1][col] == 0:
                    array[row + 1][col] = 1
                    array[row][col] = 0
                    
                random_number = random.choice([0, 1])
                    
                if random_number==0 and array[row][col]==1 and row < len(array) - 1 and col>=1 and array[row + 1][col-1]==0:
                    array[row+1][col-1]=1
                    array[row][col]=0
                elif random_number==1 and array[row][col]==1 and row < len(array)-1 and col<len(array[0])-1 and array[row+1][col+1]==0:
                    array[row+1][col+1]=1
                    array[row][col]=0      
                    


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

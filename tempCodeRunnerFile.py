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
                    
                random_number = random.choice([0, 1])
                    
                if random_number==0 and array[row][col]==1 and row < len(array) - 1 and col>=1 and array[row + 1][col-1]==0:
                    array[row+1][col-1]=1
                    array[row][col]=0
                elif random_number==1 and array[row][col]==1 and row < len(array)-1 and col<len(array[0])-1 and array[row+1][col+1]==0:
                    array[row+1][col+1]=1
                    array[row][col]=0    
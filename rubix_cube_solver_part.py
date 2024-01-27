import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame
pygame.init()

# Set the width and height of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Rubik's Cube")

# Loop until the user clicks the close button
done = False

# Use to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw the Rubik's cube state using the matrix
    for i in range(3):
        for j in range(3):
            for k in range(3):
                color = matrix[i][j][k]
                x = 100 * i
                y = 100 * j
                width = 100
                height = 100
                if color == "R":
                    pygame.draw.rect(screen, RED, [x, y, width, height])
                elif color == "G":
                    pygame.draw.rect(screen, GREEN, [x, y, width, height])
                elif color == "B":
                    pygame.draw.rect(screen, BLUE, [x, y, width, height])
                else:
                    pygame.draw.rect(screen, BLACK, [x, y, width, height])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Generate a random starting configuration for the Rubik's cube
matrix = generate_random_matrix()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Handle mouse clicks and drags to rotate the Rubik's cube
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            if start_pos[0] < end_pos[0]:
                matrix = rotate_right(matrix)
            elif start_pos[0] > end_pos[0]:
                matrix = rotate_left(matrix)
            elif start_pos[1] < end_pos[1]:
                matrix = rotate_down(matrix)
            elif start_pos[1] > end_pos[1]:
                matrix = rotate_up(matrix)

    # --- Game logic should go here

    # Check if the player has solved the Rubik's cube
    if is_solved(matrix):
        print("Congratulations, you solved the Rubik's cube!")
        done = True

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw the Rubik's cube state using the matrix
    for i in range(3):
        for j in range(3):
            for k in range(3):
                color = matrix[i][j][k]
                x = 100*i
                y = 100*j
                width = 100
                height = 100
                if color == "R":
                    pygame.draw.rect(screen, RED, [x, y, width, height])
                elif color == "G":
                    pygame.draw.rect(screen, GREEN, [x, y, width, height])
                elif color == "B":
                    pygame.draw.rect(screen, BLUE, [x, y, width, height])
                else:
                    pygame.draw.rect(screen, BLACK, [x, y, width, height])

    # ---

# Close the window and quit.
pygame.quit()

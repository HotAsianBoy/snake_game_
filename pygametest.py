import pygame
import random

# Initialize Pygame and the mixer module
pygame.init()
pygame.mixer.init()

# Screen setup
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Snake Game with Sound")

# Load sound effects
eat_sound = pygame.mixer.Sound("Cartoon Chomp Sound Effect.mp3")
# Sound for eating food


# Load background music
pygame.mixer.music.load("background_music.mp3")

# Set volume (optional)
eat_sound.set_volume(0.5)
game_over_sound.set_volume(0.5)
pygame.mixer.music.set_volume(0.3)

# Play background music (loop indefinitely)
pygame.mixer.music.play(-1)

# Game variables
snake_x = 480
snake_y = 340
snake_x_change = 0
snake_y_change = 0
snake_list = []
snake_length = 1
food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
food_y = round(random.randrange(20, 720 - 20) / 20) * 20
score = 0
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Handle key presses for snake movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        eat_sound.play()  # Play eating sound
        food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
        food_y = round(random.randrange(20, 720 - 20) / 20) * 20
        snake_length += 1
        score += 1

    # Check for collision with walls or itself
    if (snake_x >= 1000 or
            snake_x < 0 or
            snake_y >= 720 or
            snake_y < 0):
        game_over = True

    snake_head = [snake_x, snake_y]
    if snake_head in snake_list[:-1]:
        game_over = True

    # Game over logic
    if game_over:
        pygame.mixer.music.stop()  # Stop background music
        game_over_sound.play()  # Play game over sound
        pygame.time.wait(2000)  # Wait for 2 seconds
        pygame.quit()
        quit()

    # Update snake list
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    for segment in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [segment[0], segment[1], 20, 20])
    pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, 20, 20])
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(10)

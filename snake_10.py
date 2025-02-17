"""Component 4 (Food) - Further Development: add sprite"""
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - by Gideon Wong")


# Coordinates containing the colors to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)
yellow = (255, 255, 0)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves


# Create snake - replaces the previous snake drawing section in main loop
def draw_snake(snake_list):
    print(f"Snake list: {snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


def message(msg, txt_colour, bkgd_colour,):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


def game_loop():
    quit_game = False
    game_over = False

    # Snake will be in 20 x 20 pixels to work in a 20px grid
    snake_x = 480   # Centre point horizontally is (1000/2)-20 = 480
    snake_y = 340   # Centre point vertically is (720/2)-20 = 340

    snake_x_change = 0  # Holds the value of changes in the x-coordinate
    snake_y_change = 0  # Holds the value of changes in the y-coordinate
    snake_list = []
    snake_length = 1

    # Setting a random position for the food to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            screen.fill(white)
            message("You Died! Press 'Q' to quit or 'A' to play again,",
                    black, white)
            pygame.display.update()

            # Check if the user wants to 'Q' = quit, or 'A' = play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()     # Restart the game loop

        # Handling response if user presses 'X' - giving them the option to
        # quit, start a new game, or keep playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to quit, SPACE to resume, R to reset"
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # If user presses 'X' button, game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True

                        # If user presses 'R' button again, game is reset
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()

                        # If user presses the space-bar, game continues
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                end = True

                        # If user presses 'Q' game quits
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                end = True

            # Snake movement keys
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

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        # Create snake (replaces simple rectangle in original version)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        # Using a sprite (instead of a previous circle) to represent food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        # Collision for when the snake touches the food
        # Print lines are for testing
        print(f"Snake x: {snake_x}")
        print(f"Food x: {food_x}")
        print(f"Snake y: {snake_y}")
        print(f"ood y: {food_y}")
        print("\n\n")
        # Radius is subtracted from food coordinates, otherwise it
        # detects the edge of the snake and the centre of the food (circle) as
        # the collision point
        if snake_x == food_x and snake_y == food_y:
            # Set a new random position for the food to be placed
            food_x = round(random.randrange(20, 1000-20)/20) * 20
            food_y = round(random.randrange(20, 720-20)/20) * 20
            # For testing purposes
            print("Got it!")
            # Increases length of snake (by original size)
            snake_length += 1

        clock.tick(15)  # Sets the speed of which iteration of the game loop
        # run at in frames per second (in which case, the higher the number,
        # the faster and smoother it runs

    pygame.quit()
    quit()


# Main routine
game_loop()

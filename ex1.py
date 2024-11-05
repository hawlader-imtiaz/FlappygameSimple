import pgzrun  # Import the game library
import random  # Import random for random height generation

WIDTH = 350  # Set the window width
HEIGHT = 600  # Set the window height

GAP_SIZE = 250  # Set the gap size to give more space for the bird to pass

background = Actor('background')  # Load the background image
bird = Actor('bird')  # Load the bird image
bird.x = 50  # Set the bird's x coordinate
bird.y = HEIGHT / 2  # Set the bird's y coordinate

# Load the upper and lower obstacle images
bar_up = Actor('bar_up')
bar_down = Actor('bar_down')

# Initial x position for obstacles
bar_up.x = WIDTH
bar_down.x = WIDTH

score = 0  # Initialize score

# Initialize random speeds for obstacles
speed_up = random.randint(2, 4)
speed_down = random.randint(2, 4)


def draw():  # Drawing function, executed every frame
    background.draw()  # Draw the background
    bar_up.draw()  # Draw the upper part of the obstacle
    bar_down.draw()  # Draw the lower part of the obstacle
    bird.draw()  # Draw the bird
    screen.draw.text(str(score), (30, 30), fontsize=50, color="green")  # Draw score


def update():  # Update function, executed every frame
    global score, speed_up, speed_down

    # Simulate gravity for the bird
    bird.y += 3

    # Move obstacles to the left with their own random speeds
    bar_up.x -= speed_up
    bar_down.x -= speed_down

    # Reset obstacles and score when they move out of view
    if bar_up.x < -bar_up.width:
        bar_up.x = WIDTH
        bar_down.x = WIDTH

        # Randomize height and orientation for new obstacles
        gap_start = random.randint(100, HEIGHT - GAP_SIZE - 100)
        bar_up.y = gap_start - bar_up.height // 2  # Position upper bar based on gap start
        bar_down.y = gap_start + GAP_SIZE + bar_down.height // 2  # Position lower bar below gap

        # Randomize new speeds for each obstacle
        speed_up = random.randint(2, 4)
        speed_down = random.randint(2, 4)

        # Increment score and increase speed randomly for variation
        score += 1

    # Check for collisions with obstacles
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) or bird.y > HEIGHT or bird.y < 0:
        print('Game Over!')  # Display "Game Over"
        reset_game()  # Reset game state


def on_mouse_down():  # Run when mouse is clicked
    bird.y -= 100  # Make the bird jump up


def reset_game():
    global score, speed_up, speed_down

    # Reset game elements
    score = 0  # Reset score
    bird.y = HEIGHT / 2  # Reset bird position
    bar_up.x = WIDTH  # Reset upper obstacle position
    bar_down.x = WIDTH  # Reset lower obstacle position

    # Randomly place obstacles within the valid height range
    gap_start = random.randint(100, HEIGHT - GAP_SIZE - 100)
    bar_up.y = gap_start - bar_up.height // 2
    bar_down.y = gap_start + GAP_SIZE + bar_down.height // 2

    # Set new random speeds for the obstacles
    speed_up = random.randint(2, 4)
    speed_down = random.randint(2, 4)


pgzrun.go()  # Start the game loop

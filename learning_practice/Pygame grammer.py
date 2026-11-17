import pygame

# Quick formatting shortcut keys: ctrl + alt + l


# 1. Setting up a game window:

# 1.1 Initialization
pygame.init()

# 1.2 Creating a game window
win = pygame.display.set_mode((800, 600))

# 1.3 Creating a game title
pygame.display.set_caption("Pygame")

# 1.4 Turning off the system typing mode
pygame.key.stop_text_input()


# 2. Setting game background

# 2.1 Setting music
# Setting music
pygame.mixer.music.load("bgm.wav") 
# Load the music file into memory
pygame.mixer.music.play(-1)        

# 2.2 Setting background photo
# Setting background photo
bg_img = pygame.image.load("background.png") 
# Load the image file into memory
bg_img = pygame.transform.scale(bg_img, (win_w, win_h)) 

# 2.3 Loading the game background information
# Loading the game background information
player_img = pygame.image.load("me1.png").convert_alpha() 

# 2.4 Obtaining the actual size of the image# Obtaining the actual size of the image
player_w, player_h = player_img.get_size() 

# 2.5 The time for generating enemy aircraft
# 1000ms = 1s
enemy_spawn_time = 1000
# Recording the initial time
last_enemy_spawn_time = pygame.time.get_ticks()

# 2.6 Controlling the frame rate of the game
clock = pygame.time.Clock()

# 3. Game loop and handling:

# Main loop
running = True
while running:
    # Setting the background color
    win.fill((255, 255, 255))

    # Detecting and obtaining the events
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    # 4. Drawing graphics and text:
    red = (255, 0, 0)
    # Draw shapes      pygame.Rect(x, y, w, h)
    pygame.draw.rect(win, red, (100, 50, 80, 60))
    win.blit(player_img, (player_x, player_y)) 
    # Refresh the interface    update(part of screen); flip(whole screen)
    pygame.display.flip()
    # Refresh frame rate
    pygame.time.Clock().tick(60)

    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello game!", True, (0, 0, 255))
    # tags     (text, position)
    win.blit(text, (325, 10))

# Game over
pygame.quit()

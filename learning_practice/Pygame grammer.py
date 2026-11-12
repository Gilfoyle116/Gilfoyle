import pygame

# Quick formatting shortcut keys: ctrl + alt + l


# 1. Setting up a game window:

# Initialization
pygame.init()

# Creating a game window
win = pygame.display.set_mode((800, 600))

# Creating a game title
pygame.display.set_caption("Pygame")


# 2. Game loop and handling:

# Main loop
running = True
while running:
    # Detecting and obtaining the events
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    # 3. Drawing graphics and text:
    white = (255, 255, 255)
    # Draw shapes      pygame.Rect(x, y, w, h)
    pygame.draw.rect(win, white, pygame.Rect(100, 50, 80, 60))
    # Refresh the interface    update(part of screen); flip(whole screen)
    pygame.display.flip()

    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello game!", True, (255, 255, 255))
    # tags     (text, position)
    win.blit(text, (325, 10))

# Game over
pygame.quit()

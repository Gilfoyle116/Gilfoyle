import pygame

pygame.init()

# Disable input method capture
pygame.key.stop_text_input()

# Game window size
game_x = 800
game_y = 600

win = pygame.display.set_mode((game_x, game_y))
pygame.display.set_caption("Pygame Demo")

# Player's magnitude
player_x = 100
player_y = 100
player_w = 60
player_h = 50
player_speed = 5


# Color initialization
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Player's color
player_color = blue
# Controlling the frame rate of the game
clock = pygame.time.Clock()

running = True
while running:
    win.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detecting mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Detecting left-click event
            if event.button == 1:
                player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
                # Detecting the area where the click occurred
                if player_rect.collidepoint(event.pos):
                    if player_color == blue:
                        player_color = green
                    else:
                        player_color = blue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed


    if player_x < 0:
        player_x = 0
    if player_y < 0:
        player_y = 0
    if player_x > game_x - player_w:
        player_x = game_x - player_w
    if player_y > game_y - player_h:
        player_y = game_y - player_h

    pygame.draw.rect(win, player_color, [player_x, player_y, player_w, player_h])

    font = pygame.font.Font(None, 36)
    text = font.render("Pygame Demo", True, blue)
    win.blit(text, (325, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()

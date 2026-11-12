import pygame

pygame.init()

# Game interface size
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

# Color initialization  (RGB)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)


running = True
while running:
    win.fill(white)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.draw.rect (win, black, [player_x, player_y, player_w, player_h])
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    font = pygame.font.Font(None, 36)
    text = font.render("Pygame Demo", True, black)
    win.blit(text, (425, 10))

    # Obtaining the current state of the keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Preventing player from moving beyond the boundaries
    if player_x < 0:
        player_x = 0
    if player_y < 0:
        player_y = 0
    if player_x > game_x - player_w:
        player_x = game_x - player_w
    if player_y > game_y - player_h:
        player_y = game_y - player_h

pygame.quit()
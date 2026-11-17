import pygame
import random

pygame.init()
# Disable input method capture
pygame.key.stop_text_input()

# Setting music
try:
    pygame.mixer.music.load("bgm.wav")
    pygame.mixer.music.play(-1)
except Exception:
    print("Warning: bgm.wav not found or failed to load.")

# Setting game window
win_w = 450
win_h = 800
win = pygame.display.set_mode((win_w, win_h), vsync=1)
pygame.display.set_caption("Airplane flying and shooting")

# Setting background photo
bg_img = pygame.image.load("background.png")
bg_img = pygame.transform.scale(bg_img, (win_w, win_h))

# Loading the game background information
player_img = pygame.image.load("me1.png").convert_alpha()
enemy_img = pygame.image.load("enemy1.png").convert_alpha()
bullet_img = pygame.image.load("bullet1.png").convert_alpha()

# Obtaining the actual size of the image
player_w, player_h = player_img.get_size()
enemy_w, enemy_h = enemy_img.get_size()
bullet_w, bullet_h = bullet_img.get_size()

# Setting players
player_x = win_w // 2 - player_w // 2
player_y = win_h - player_h - 30
player_speed = 8

# Bullet magnitude
bullet_speed = 12
bullets = []

# Enemy aircraft magnitude
enemy_speed = 6
enemies = []

# The time for generating enemy aircraft
# 1000ms = 1s
enemy_spawn_time = 1000
# Recording the initial time
last_enemy_spawn_time = pygame.time.get_ticks()

# Controlling the frame rate of the game
clock = pygame.time.Clock()

running = True
while running:
    # Setting background photo
    win.blit(bg_img, (0, 0))
    # Local time
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Space key: generate bullet
            if event.key == pygame.K_SPACE:
                # player's x-coordinate - half player's width + half bullet's width
                bullet_x = player_x + player_w // 2 - bullet_w // 2
                # bullet's y-coordinate equal to player's y-coordinate
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    # Getting keyboard status
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed

    # Preventing player out of the screen
    player_x = max(0, min(player_x, win_w - player_w))
    player_y = max(0, min(player_y, win_h - player_h))

    # Generating enemy aircraft
    if current_time - last_enemy_spawn_time > enemy_spawn_time:
        enemy_x = random.randint(0, win_w - enemy_w)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])
        last_enemy_spawn_time = current_time

    # Updating bullet
    # Create new bullet list to avoid remove item during traversal
    new_bullets = []
    for bullet in bullets:
        bullet[1] -= bullet_speed
        # Keep bullet if it is still inside the window
        if bullet[1] >= 0:
            new_bullets.append(bullet)
    bullets = new_bullets

    # Updating enemy
    # Create new enemy list to avoid remove item during traversal
    new_enemies = []
    for enemy in enemies:
        enemy[1] += enemy_speed
        # Keep enemy if it is still inside the window
        if enemy[1] <= win_h:
            new_enemies.append(enemy)
    enemies = new_enemies

    # Detecting collision between bullet and enemy
    # Store indexes of hit bullets and enemies
    hit_bullets = set()
    hit_enemies = set()
    for i, bullet in enumerate(bullets):
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_w, bullet_h)
        for j, enemy in enumerate(enemies):
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_w, enemy_h)
            # Determining whether there was a collision between the enemy aircraft and the bullets
            if bullet_rect.colliderect(enemy_rect):
                hit_bullets.add(i)
                hit_enemies.add(j)
                break

    # Detecting the collision between the player and the enemy aircraft
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_w, enemy_h)
        if player_rect.colliderect(enemy_rect):
            running = False
            break

    # Removing hit bullets from bullet list
    bullets = [bullets[i] for i in range(len(bullets)) if i not in hit_bullets]
    # Remove hit enemies from enemy list
    enemies = [enemies[j] for j in range(len(enemies)) if j not in hit_enemies]

    # Drawing player image
    win.blit(player_img, (player_x, player_y))

    # Drawing bullet images
    for bullet in bullets:
        win.blit(bullet_img, (bullet[0], bullet[1]))

    # Drawing enemy images
    for enemy in enemies:
        win.blit(enemy_img, (enemy[0], enemy[1]))

    # Refresh screen
    pygame.display.flip()
    # Frequency of refreshing
    clock.tick(60)

pygame.quit()
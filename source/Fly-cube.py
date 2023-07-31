import pygame
import sys
import random

# Определение констант
BACKGROUND_COLOR = (28, 36, 68)  # Темно-синий
PLAYER_SIZE = 50
ENEMY_SIZE = 50
ENEMY_SPEED = 10

# Инициализация Pygame
pygame.init()

# Создание окна игры
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height), vsync=1)
pygame.display.set_caption("Летающий квадрат")

# Загрузка спрайтов для игрока и врагов
player_image = pygame.image.load("sprites/player.png").convert_alpha()
enemy_image = pygame.image.load("sprites/enemy.png").convert_alpha()

# Масштабирование спрайтов до нужного размера
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))

# Функция для отрисовки игрока
def draw_player(player_pos):
    screen.blit(player_image, player_pos)

# Функция для отрисовки врага
def draw_enemy(enemy_pos):
    screen.blit(enemy_image, enemy_pos)

# Функция для проверки столкновения игрока и врага
def collision_check(player_pos, enemy_pos):
    player_rect = pygame.Rect(player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE)
    return player_rect.colliderect(enemy_rect)

# Функция для отображения главного меню
def main_menu():
    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                elif event.key == pygame.K_s:
                    settings_menu()
                elif event.key == pygame.K_q:  # Выход из игры при нажатии клавиши "Q"
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:  
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_x, mouse_y):
                    game_loop()
                elif settings_rect.collidepoint(mouse_x, mouse_y):
                    settings_menu()

        font = pygame.font.Font(None, 72)
        title_surface = font.render("Летающий квадрат", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(title_surface, title_rect)

        font = pygame.font.Font(None, 36)
        start_surface = font.render("Нажмите Пробел или ЛКМ, чтобы начать игру", True, (255, 255, 255))
        start_rect = start_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(start_surface, start_rect)

        settings_surface = font.render("Нажмите S или ПКМ для настроек", True, (255, 255, 255))
        settings_rect = settings_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(settings_surface, settings_rect)

        quit_surface = font.render("Нажмите Q для выхода из игры", True, (255, 255, 255))
        quit_rect = quit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        screen.blit(quit_surface, quit_rect)

        pygame.display.update()




# Функция для отображения меню настроек
# Обновленная функция settings_menu() для добавления пункта выбора разрешения
def settings_menu():
    fullscreen = False

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                    return
                elif event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    # Pass width and height to apply_settings()
                    apply_settings(fullscreen, screen_width, screen_height)
                elif event.key == pygame.K_q:  
                    pygame.quit()
                    sys.exit()


        font = pygame.font.Font(None, 72)
        title_surface = font.render("Настройки", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(title_surface, title_rect)

        font = pygame.font.Font(None, 36)
        fullscreen_surface = font.render("Нажмите F для переключения полноэкранного режима", True, (255, 255, 255))
        fullscreen_rect = fullscreen_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(fullscreen_surface, fullscreen_rect)

        back_surface = font.render("Нажмите ESC для возврата в главное меню", True, (255, 255, 255))
        back_rect = back_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(back_surface, back_rect)

        quit_surface = font.render("Нажмите Q для выхода из игры", True, (255, 255, 255))
        quit_rect = quit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        screen.blit(quit_surface, quit_rect)

        pygame.display.update()

# Функция для применения настроек (разрешение и полноэкранный режим)
def apply_settings(fullscreen, width, height):
    flags = pygame.FULLSCREEN if fullscreen else 0
    new_screen = pygame.display.set_mode((width, height), flags)

    # Scale game elements based on the screen size
    global PLAYER_SIZE, ENEMY_SIZE
    PLAYER_SIZE = width // 16
    ENEMY_SIZE = width // 16

    # Scale player and enemy images
    global player_image, enemy_image
    player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
    enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))

    return new_screen  # Возвращаем новое окно



# Код игры "Летающий квадрат"
def game_loop():
    player_pos = [screen_width // 3, screen_height // 2]
    enemy_pos = [screen_width, random.randint(0, screen_height - ENEMY_SIZE)]
    score = 0
    frame_count = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            player_pos[1] += 5

        screen.fill(BACKGROUND_COLOR)

        enemy_pos[0] -= ENEMY_SPEED
        if enemy_pos[0] < 0:
            enemy_pos[0] = screen_width
            enemy_pos[1] = random.randint(0, screen_height - ENEMY_SIZE)
            score += 1

        if collision_check(player_pos, enemy_pos):
            game_over()
            return  # Вернуться в главное меню после поражения

        draw_player(player_pos)
        draw_enemy(enemy_pos)

        font = pygame.font.Font(None, 36)
        score_surface = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))

        frame_count += 1
        fps_surface = font.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
        screen.blit(fps_surface, (10, 40))  # Отображение количества кадров на экране

        pygame.display.update()
        clock.tick(60)  # Уменьшено до 60 кадров в секунду

def game_over():
    font = pygame.font.Font(None, 72)
    game_over_surface = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(game_over_surface, game_over_rect)

    font = pygame.font.Font(None, 36)
    back_surface = font.render("Нажмите ESC для возврата в главное меню или Q для выхода", True, (255, 255, 255))
    back_rect = back_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(back_surface, back_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Возврат к главному меню при нажатии клавиши "ESC"
                    main_menu()
                    return
                elif event.key == pygame.K_q:  # Выход из игры при нажатии клавиши "Q"
                    pygame.quit()
                    sys.exit()


main_menu()

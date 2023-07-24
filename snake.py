import pygame
import time
import random

pygame.init()

# Definição das cores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Configuração da tela
display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Jogo da Cobrinha')
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 8

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

def game_loop():
    game_over = False
    game_close = False

    snake_list = []
    length_of_snake = 1

    # Posição inicial da cobra
    snake_x = display_width / 2
    snake_y = display_height / 2

    # Movimento inicial da cobra
    snake_x_change = 0
    snake_y_change = 0

    # Posição aleatória da comida
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(blue)
            message("SE FUDEU! Pressione Q-Sair ou C-Jogar Novamente", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        # Verificar colisões com as bordas da tela
        if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        game_display.fill(blue)
        pygame.draw.rect(game_display, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Verificar colisão da cobra com ela mesma
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Desenhar a cobra
        for segment in snake_list:
            pygame.draw.rect(game_display, , [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        # Verificar se a cobra pegou a comida
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

# initialize pygame======
import pygame
import random
import os

pygame.mixer.init()
pygame.mixer.music.load('start.mp3')
pygame.mixer.music.play()


x=pygame.init()



# print(x)
# ==========testing above==============

# color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

# =====window setup====
screen_width=900
screen_height=600
gameWindow= pygame.display.set_mode((screen_width, screen_height))

# background====
bgimg=pygame.image.load("original.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
# title===
pygame.display.set_caption("Snake Game")

# screen display score function
font = pygame.font.SysFont(None, 55)

# clock record
clock = pygame.time.Clock()

# ================score==========
def text_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# ================wlcome to game==============

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,233,200))

        text_score("Wlecome to Snake Game", red, 170, 190)
        text_score("Press Space Bar to play", red, 200, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(50)



# creating a game loop====
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30

    fps = 50
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(10, screen_width / 2)
    food_y = random.randint(15, screen_height / 2)
    score = 0
    init_velocity = 5

# ========if file not exists=============
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()


# ==========length function=======
    def plot_snake(gameWindow, black, snk_list, snake_size):
        for x, y in snk_list:
            pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

    snk_list = []
    snk_length = 1


    while not exit_game:

        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            text_score("Game over! Press Enter to Enter", white, 150, 300)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.Key ==pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x= init_velocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key == pygame.K_DOWN:
                        velocity_y= init_velocity
                        velocity_x=0

                    if event.key==pygame.K_q:
                        score+=5

            snake_x= snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score+=10
# ==============to generate randomly foo of snake============
                food_x = random.randint(10, screen_width / 2)
                food_y = random.randint(15, screen_height / 2)
                snk_length+=5

                if score>int(hiscore):
                    hiscore=score

            gameWindow.fill((32,178,170))
            gameWindow.blit(bgimg,(0,0))

            plot_snake(gameWindow,black,snk_list, snake_size)

            text_score("Score: "+ str(score)+ "Hiscore"+ str(hiscore), red, 5, 5)
# =======to attach head as snake eat ...for growth======
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

# ==========    when snake touch his own body it will game over===========
            if head in snk_list[:-1]:
                game_over=True

                pygame.mixer.music.load('Over.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

                pygame.mixer.music.load('Over.mp3')
                pygame.mixer.music.play()
#=========== food draws============
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()

# call function to show game
welcome()
game_loop()
# pygame template
import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

BROWN = (222, 184, 135)
BROWNT = (139, 69, 19)
BROWNTR = (210, 105, 30)
BLUE = (135, 206, 250)
BLUET = (30, 144, 255)
YELLOW = (255, 255 , 0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GRAYT = (128, 121, 121)
ORANGE = (255, 140, 0)
WHITE = (255, 255, 255)


flicker_interval = 8
a = 0
e = BLACK
day = True
night = False
circle_x = 0
circle_y = 70
radius = 30


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    a = random.randint(1, 1000)
    
    # DRAWING
    if day:
        e = BLACK
        screen.fill(BLUE)  # always the first drawing command
        pygame.draw.circle(screen, YELLOW, (circle_x - 30, circle_y), radius)
        pygame.draw.circle(screen, ORANGE, (circle_x - 30, circle_y), radius - 3)

        circle_x += 2
        if circle_x >= WIDTH + 2 * radius:
            day = False
            night = True
            circle_x = 0

    elif night:
        if a % flicker_interval == 0:
            e = BLACK
        else:
            e = YELLOW 
        screen.fill(BLACK)  # always the first drawing command
        pygame.draw.circle(screen, GRAY, (circle_x - 30, circle_y), radius)
        pygame.draw.circle(screen, GRAYT, (circle_x - 40, circle_y + 5), radius - 20)
        pygame.draw.circle(screen, GRAYT, (circle_x - 20, circle_y + - 8), radius - 25)

        circle_x += 2
        if circle_x >= WIDTH + 2 * radius:
            night = False
            day = True
            circle_x = 0

    x = - 25
    pygame.draw.rect(screen, GREEN, (0, 280, 640, 200))
    pygame.draw.ellipse(screen, ORANGE, (460, 230 + x, 120, 100))
    pygame.draw.circle(screen, e, (495, 267 + x), 10)
    pygame.draw.circle(screen, e, (540, 265 + x), 10)
    pygame.draw.ellipse(screen, e, (495, 296 + x, 50, 20))
    pygame.draw.polygon(screen, e, ((519, 277 + x), (510, 288 + x), (527, 288 + x)))
    pygame.draw.polygon(screen, GREEN, ((513, 217 + x), (530, 217 + x), (534, 238 + x), (506, 237 + x)))
    
    for i in range(3):
        pygame.draw.rect(screen, BROWN, (i * 130 + 20, 170, 80, 110))
        pygame.draw.rect(screen, BROWNTR, (i * 130 + 70, 131, 20, 40))
        pygame.draw.polygon(screen, BROWNT, ((i * 130 + 20, 170), (i * 130 + 100, 170), ((i * 130 * 2 + 120) / 2, 140)))
        pygame.draw.rect(screen, BROWNTR, (i * 130 + 40, 230, 80 // 3, 50))
        pygame.draw.ellipse(screen, GRAY, (i * 130 + 55, 185, 30, 30))
        pygame.draw.circle(screen, BROWNT, (i * 130 + 58, 260), 5)
        pygame.draw.rect(screen, BLACK, (i * 130 + 55, 199, 30, 2))
        pygame.draw.rect(screen, BLACK, (i * 130 + 69, 185, 2, 30))


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)

    #---------------------------


pygame.quit()
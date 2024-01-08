import pygame
from pygame.locals import * #importing everything from locals(to use keyboard)

pygame.init()
screen = pygame.display.set_mode((1030, 500))
pygame.display.set_caption("Breaking Bricks")
clock = pygame.time.Clock()

# Bat
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha() # convert the surface as same pixel format as the image
bat_rect = bat.get_rect() # to determine where the paddle is on the screen(height of the rectangle pixel)
bat_rect[1] = screen.get_height() - 50 # to place the bat 50 pixels from bottom of the screen
#a, b = bat_rect[0], bat_rect[1]

# Ball
ball = pygame.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect() # note rect has x, y, width, height
ball_start = (200, 200) # initial position of the ball
ball_speed = (3.0, 3.0)
ball_served = False # initally we want the ball be static unless we ask it to move
sx, sy = ball_speed # speed in the x and y direction
ball_rect.topleft = ball_start # position the ball at start point (topleft is a feature in rect)

#Brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_gap = 10
brick_row = 5
# lets make sure the bricks are loaded to the entire screen width
brick_col = screen.get_width() // brick_rect[2] + brick_gap # // is integer division for rounding point
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_col + brick_gap) // 2
for y in range(brick_row):
 #   if y < screen.get_height() - brick.get_height():
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_col):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))


game_over = False

while not game_over:
    screen.fill((0, 0, 0))
    dt = clock.tick(50) # game runs in 50 frames per second
    for b in bricks:
        screen.blit(brick, b)
    screen.blit(bat, bat_rect) # display bat on the screen
    screen.blit(ball, ball_rect)

    pressed = pygame.key.get_pressed()

    if pressed[K_LEFT]: # left key
        bat_rect[0] = bat_rect[0] - 0.5 * dt # move bat left
    if pressed[K_RIGHT]: # right key
        bat_rect[0] = bat_rect[0] + 0.5 * dt # move bat right
    if pressed[K_SPACE]:
        ball_served = True

    #Setting framses so ball wont go out of screen

    if ball_rect[0] > (screen.get_width()-ball.get_width()): #right
        ball_rect[0] = screen.get_width()-ball.get_width()
        sx = sx * (-1) # bounce the ball back in opposite direction
    if ball_rect[1] > (screen.get_height()-ball.get_height()): #bottom
        ball_rect[1] = screen.get_height()-ball.get_height()
        sy = sy * (-1) # bounce the ball back in opposite direction
    if ball_rect[0] < 0: #left
        ball_rect[0] = 0
        sx = sx * (-1) # bounce the ball back in opposite direction
    if ball_rect[1] < 0: #top
        ball_rect[1] = 0
        sy = sy * (-1) # bounce the ball back in opposite direction

    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()

pygame.quit()



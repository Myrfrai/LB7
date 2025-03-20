import pygame as pg
import sys

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ball_rad = 25
step = 20

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Move the Ball")
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and ball_y - ball_rad > 0:
        ball_y -= step
    if keys[pg.K_DOWN] and ball_y + ball_rad < SCREEN_HEIGHT:
        ball_y += step
    if keys[pg.K_LEFT] and ball_x - ball_rad > 0:
        ball_x -= step
    if keys[pg.K_RIGHT] and ball_x + ball_rad < SCREEN_WIDTH:
        ball_x += step

    
    screen.fill((255, 255, 255))
    pg.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_rad)
    pg.display.flip()
    clock.tick(60)
pg.quit()

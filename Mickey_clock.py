import pygame as pg
import datetime

pg.init()
screen = pg.display.set_mode((800, 600))

clock_image = pg.image.load('mouse/clock.png')
minute_hand = pg.image.load('mouse/rightarm.png')
second_hand = pg.image.load('mouse/leftarm.png')

clock_image = pg.transform.scale(clock_image, (800, 600))
minute_hand = pg.transform.scale(minute_hand, (900, 600))
second_hand = pg.transform.scale(second_hand, (50, 600))

done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill((255, 255, 255))
    
    screen.blit(clock_image, (0, 0))
    
    now = datetime.datetime.now()
    min = now.minute
    sec = now.second 
    mangle = -6 * min
    sangle = -6 * sec
    
    rotated_mhand = pg.transform.rotate(minute_hand, mangle)
    rotated_shand = pg.transform.rotate(second_hand, sangle)
    
    minute_rect = rotated_mhand.get_rect(center=(400, 300))
    second_rect = rotated_shand.get_rect(center=(400, 300))
    
    screen.blit(rotated_mhand, minute_rect.topleft)
    screen.blit(rotated_shand, second_rect.topleft)
    
    pg.display.flip() 
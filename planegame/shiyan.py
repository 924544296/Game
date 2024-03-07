import pygame as pg 

pg.init()
screen = pg.display.set_mode((45,80))
image = pg.image.load('I:/python/code/escape/images/astronaut.png')
screen.blit(image, (0,0))
pg.display.update()
while 1:
    pass
pg.quit()
import random 
import pygame as pg 


SCREEN_RECT = pg.Rect(0, 0, 480, 700)
FRAME_RATE = 60
CREATE_ENEMY_EVENT = pg.USEREVENT
HERO_FIRE_EVENT = pg.USEREVENT + 1


class MySprite(pg.sprite.Sprite):
    #
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pg.image.load(image_name)
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speed = speed
    #
    def update(self):
        self.rect.y += self.speed


class Background(MySprite):
    #
    def __init__(self, is_alter=False):
        super().__init__(image_name='./images/background.png', speed=1)
        if is_alter:
            self.rect.y = -self.rect.height
    #
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(MySprite):
    #
    def __init__(self):
        super().__init__(image_name='./images/enemy1.png', speed=random.randint(1,3))
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.bottom = 0
    #
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    #
    # def __del__(self):
    #     pass


class Hero(MySprite):
    #
    def __init__(self):
        super().__init__(image_name='./images/me1.png', speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.group_bullet = pg.sprite.Group()
    #
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_RECT.width-self.rect.width:
            self.rect.x = SCREEN_RECT.width-self.rect.width
    #
    def fire(self):
        for i in range(3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            self.group_bullet.add(bullet)


class Bullet(MySprite):
    #
    def __init__(self):
        super().__init__(image_name='./images/bullet1.png', speed=-2)
    #
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
    #
    # def __del__(self):
    #     pass
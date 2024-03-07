import pygame as pg 
from plane_sprites import * 


class PlaneGame(object):
    #
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_RECT.size)
        pg.display.set_caption('Plane War')
        pg.display.set_icon(pg.image.load('./images/icon.ico'))
        self.clock = pg.time.Clock()
        self.__create_sprites()
        pg.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pg.time.set_timer(HERO_FIRE_EVENT, 500)
        self.screen_id = 0 # 0:welcome 1:run 2:pause 3:game over
    #
    def __create_sprites(self):
        #
        background1 = Background()
        background2 = Background(is_alter=True)
        self.group_background = pg.sprite.Group(background1, background2)
        self.group_background.update()
        self.group_background.draw(self.screen)
        #
        self.group_enemy = pg.sprite.Group()
        #
        self.hero = Hero()
        self.group_hero = pg.sprite.Group(self.hero)
    #
    def start_game(self):
        while 998:
            self.clock.tick(FRAME_RATE)
            #
            self.__event_handler()
            #
            self.__check_collide()
            #
            self.__update_sprites()
            #
            pg.display.update()
    #
    def __event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.group_enemy.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]:
            self.hero.speed = -2
        elif keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]:
            self.hero.speed = 2
        else:
            self.hero.speed = 0
    #
    def __check_collide(self):
        pg.sprite.groupcollide(self.group_enemy, self.hero.group_bullet, True, True, pg.sprite.collide_mask)
        is_collide = pg.sprite.groupcollide(self.group_enemy, self.group_hero, True, True, pg.sprite.collide_mask)
        if len(is_collide) > 0:
            self.hero.kill()
            PlaneGame.__game_over()
    #
    def __update_sprites(self):
        #
        self.group_background.update()
        self.group_background.draw(self.screen)
        #
        self.group_enemy.update()
        self.group_enemy.draw(self.screen)
        #
        self.group_hero.update()
        self.group_hero.draw(self.screen)
        #
        self.hero.group_bullet.update()
        self.hero.group_bullet.draw(self.screen)
    #
    @staticmethod
    def __game_over():
        pg.quit()
        exit()
    #
    #


# ===================================================
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
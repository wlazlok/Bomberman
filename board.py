import os
import sys

import pygame as py, config, bomb, threading, enemy, endGame, final, time

walls = []  # lista ze wspolrzednymi scian
bomb_xy = []  # lista ze wspolrzednymi bomb
bomb_id = {}
brick = []  # lista ze wspolrzednymi scian mozliwymi do zniszczenia
doors = []  # lista ze wspolrzednymi dzrwi
enemy_xy = []  # lista ze wspolrzednymi przeciwnikow
bomb_powerup = []  # lista ze wspolrzednymi power-upów
life_pick = []  # lista ze wspolrzednymi dodatkowych zyc
add_bomb = []  # lista ze wspolrzednymi dodatkowymi bombami
enemies_alive = []  # lista z zyjacymi przeciwnikami
bomb_threads = []  # lista z watkami bomb


# funkcja rysujaca drzwi
def draw_doors():
    doors_img = py.image.load('images/tiles/doors_locked.png').convert()
    config.screen.blit(doors_img, doors[0])
    config.flaga = True


# funkcja czyszczaca listy
def clear():
    walls.clear()
    brick.clear()
    bomb_powerup.clear()
    life_pick.clear()
    add_bomb.clear()
    enemies_alive.clear()
    doors.clear()


class Board:
    def __init__(self, player):

        config.clearBackground()
        config.screen = py.display.set_mode((1024, 680))
        config.screen.fill((81, 81, 81))

        self.alive = config.enemy_alive
        self.running = True
        self.door_opened = False
        self.moveXD = False
        self.enemiesXY = []
        self.player = player

        self.img = py.image.load('images/tiles/ground.png').convert()
        self.doors = py.image.load('images/tiles/doors.png').convert()
        self.doors_open = py.image.load('images/tiles/doors_open.png').convert()
        self.backToMenu = py.image.load('images/do_menu.png').convert()
        self.again = py.image.load('images/again.png').convert()

        py.mixer.music.load('sounds/leveltheme.mid')
        py.mixer.music.play(-1)
        py.mixer.music.set_volume(config.volume)

    def return_doors(self):
        return self.door_opened

    def actual_level(self):
        return config.actual_level

    # metoda ustawiajaca wspolrzedne gracza na poczatkowe wartosci i rysujaca go od nowa
    def die(self):
        self.player.x, self.player.y = 40, 40
        config.screen.blit(self.player.image_start, (40, 40))

    # metoda
    def draw(self, level, b):
        self.player.x, self.player.y = 40, 40
        # self.start_ticks = py.time.get_ticks()

        file = open(str(level), "r").read().split('\n')

        x, y = 0, 0
        for row in file:
            x = 0
            for col in row:
                if str(col) == str(1):
                    img = py.image.load('images/tiles/slate.png').convert()
                    config.screen.blit(img, (x, y))
                    walls.append((x, y))

                elif str(col) == str(2) or str(col) == str(3) or str(col) == str(4) or str(col) == str(5):
                    img = py.image.load('images/tiles/1.png').convert()
                    config.screen.blit(img, (x, y))
                    brick.append((x, y))
                    if str(col) == str(2):
                        bomb_powerup.append((x, y))
                    elif str(col) == str(3):
                        life_pick.append((x, y))
                    elif str(col) == str(4):
                        add_bomb.append((x, y))
                    elif str(col) == str(5):
                        doors.append((x, y))

                else:
                    img = py.image.load('images/tiles/ground.png').convert()
                    config.screen.blit(img, (x, y))
                x = x + 40

            y = y + 40

        act_level = self.actual_level()
        for i in range(act_level + 3):
            if i == 0:
                continue
            e = enemy.Enemy(i, b)
            enemies_alive.append(e)

        clock = py.time.Clock()

        self.seconds = 200
        milliseconds = 0

        config.screen.blit(self.player.image_start, (40, 40))

        while self.running:


            if milliseconds > 1000:
                self.seconds -= 1
                milliseconds -= 1000

            milliseconds += clock.tick_busy_loop(60)

            if self.seconds == 0:
                for n in enemies_alive:
                    n.alive = False

                self.door_opened = False
                if b.score != 0:
                    open("highscores.txt", "a").write(str(b.score) + "\n")
                clear()
                self.door_opened = False

                config.flaga = False
                endGame.EndGame()
                break

            if config.actual_level == 5:
                if self.door_opened and (b.x, b.y) == doors[0]:
                    self.door_opened = False
                    for n in enemies_alive:
                        n.alive = False
                    open("highscores.txt", "a").write(str(b.score) + "\n")
                    clear()
                    final.Final(b)
                    break

            self.gui()

            for i in enemies_alive:
                self.enemiesXY.append(i.getEXY())
            if not self.moveXD:
                config.screen.blit(b.image_start, (40, 40))
            if (b.x, b.y) in self.enemiesXY:
                b.lives -= 1
                self.die()

            # jesli wejdziemy w zasieg wybuchu bomby tracimy zycie
            if (b.x, b.y) in bomb.explode_range:
                b.lives -= 1
                bomb.explode_range.clear()
                self.die()

            # jestli mamy 0 zyc gra sie konczy
            if b.lives <= 0:
                for n in enemies_alive:
                    n.alive = False

                self.door_opened = False
                if b.score != 0:
                    open("highscores.txt", "a").write(str(b.score) + "\n")
                clear()
                self.door_opened = False

                config.flaga = False
                endGame.EndGame()
                break

            # jesli zabijemy przeciwnikow otwieraja sie drzwi
            if config.enemy_alive == 0:
                if config.flaga:
                    config.screen.blit(self.doors_open, doors[0])
                self.door_opened = True

            # jesli drzwi sa otwarte oraz stoimy na nich przechodzimy na nastepny poziom
            if self.door_opened and (b.x, b.y) == doors[0]:
                clear()
                config.actual_level += 1
                self.alive = config.actual_level + 3
                self.door_opened = False
                config.enemy_alive = config.actual_level + 2
                b.currentBomb += 20
                config.flaga = False
                self.draw(config.actual_level, b)
                break

            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        if b.currentBomb > 0:
                            x, y = b.getXY()
                            bomb_xy.append(b.getXY())

                            bomb1 = threading.Thread(target=bomb.Bomb,
                                                     args=(x, y, b.power, self.door_opened, self.player))
                            bomb1.start()
                            b.currentBomb -= 1
                            bomb_threads.append(bomb1)

                    # cheat kill enemies
                    if event.key == py.K_k:
                        for n in enemies_alive:
                            n.alive = False
                        enemies_alive.clear()
                        self.door_opened = True
                        config.flaga = True
                        config.screen.blit(self.doors_open, doors[0])

                    else:
                        self.moveXD = True
                        b.movement(event.key)

            self.enemiesXY.clear()
            py.display.update()
            py.display.flip()


    def gui(self):

        img = py.image.load('images/tlo.png').convert()
        config.screen.blit(img, (920, 35))
        config.screen.blit(img, (920, 600))

        timer = py.image.load('images/timer.png').convert()
        config.screen.blit(timer, (925, 620))

        bomb_counter = py.image.load('images/bomb.png').convert()
        life = py.image.load('images/tiles/life.png').convert()

        config.screen.blit(bomb_counter, (930, 130))
        config.screen.blit(life, (930, 180))

        text_timer = config.font.render(str(self.seconds), True, (255, 0, 1), (81, 81, 81))
        text_timer_rect = text_timer.get_rect()
        text_timer_rect.center = (990, 650)

        text = config.font.render(str(self.player.currentBomb), True, (255, 0, 1), (81, 81, 81))
        textrect = text.get_rect()
        textrect.center = (990, 155)

        text_life = config.font.render(str(self.player.lives), True, (255, 0, 1), (81, 81, 81))
        text_life_rect = text_life.get_rect()
        text_life_rect.center = (990, 185)

        config.screen.blit(text, textrect)
        config.screen.blit(text_life, text_life_rect)
        config.screen.blit(text_timer, text_timer_rect)

        text = config.font2.render("Score:", True, (255, 0, 1), (81, 81, 81))
        score = config.font.render(str(self.player.score), True, (255, 0, 1), (81, 81, 81))
        textrect = text.get_rect()
        textrect.center = (970, 55)
        config.screen.blit(text, textrect)

        scorerect = score.get_rect()
        scorerect.center = (970, 85)
        config.screen.blit(score, scorerect)

        liferect = life.get_rect()
        liferect.center = (970, 115)

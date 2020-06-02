

import pygame as py, highscore, instructions, config, play
from pygame import mixer



class Titlescreen:

    def __init__(self):


        self.running = True
        self.sub_running = False

        self.button_choosen_id = 0
        self.button_choosen = {0: 'images/titlescreen_play.png', 1: 'images/titlescreen_instructions.png',
                               2: 'images/titlescreen_highscores.png', 3: 'images/titlescreen_exit.png'}

        self.backToMenu = py.image.load('images/do_menu.png').convert()
        self.again = py.image.load('images/again.png').convert()

        imagePath = self.button_choosen[self.button_choosen_id]
        img = py.image.load(imagePath).convert()
        config.screen.blit(img, (0, 0))
        py.display.flip()

        while self.running:
            py.init()
            config.screen  # = py.display.set_mode((1024, 768))
            py.display.set_caption("Bomberman")

            icon = py.image.load('images/icon.png')
            py.display.set_icon(icon)

            vol = py.mixer.music.get_volume()
            text = config.font.render(str(round(vol, 1)), True, (255, 245, 1), (81, 81, 81))
            textRect = text.get_rect()
            textRect.center = (950, 726)
            config.screen.blit(text, textRect)
            py.display.update()

            config.fps

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_DOWN and not self.sub_running:
                        self.button_choosen_id += 1
                        if self.button_choosen_id == 4:
                            self.button_choosen_id -= 4
                        imagePath = self.button_choosen[self.button_choosen_id]
                        img = py.image.load(imagePath).convert()
                        config.screen.blit(img, (0, 0))
                        py.display.flip()

                    if event.key == py.K_UP and not self.sub_running:
                        self.button_choosen_id -= 1
                        if self.button_choosen_id < 0:
                            self.button_choosen_id += 4
                        imagePath = self.button_choosen[self.button_choosen_id]
                        img = py.image.load(imagePath).convert()
                        config.screen.blit(img, (0, 0))
                        py.display.flip()

                    if event.key == py.K_RIGHT:
                        if vol < 1:
                            vol += 0.1
                            py.mixer.music.set_volume(round(vol,1))
                            config.volume += 0.1
                        else:
                            pass

                    if event.key == py.K_LEFT:
                        if vol > 0:
                            vol -= 0.1
                            config.volume -= 0.1
                            py.mixer.music.set_volume(round(vol,1))
                        else:
                            pass

                    if event.key == py.K_RETURN:
                        if self.button_choosen_id == 3:
                            self.running = False
                            py.quit()

                        if self.button_choosen_id == 2:
                            self.sub_running = True
                            h = highscore.Highscore()
                            h.displayScore()
                            self.running = False

                        if self.button_choosen_id == 1:
                            self.sub_running = True
                            instructions.Instructions()
                            self.running = False

                        if self.button_choosen_id == 0:
                            self.sub_running = True
                            play.Play(1)
                            self.running = False




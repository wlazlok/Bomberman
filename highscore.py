import pygame as py
import titlescreen
import config, os


class Highscore:
    def __init__(self):

        self.running = True
        self.file = open('highscores.txt', "r").read().split('\n')

        imagePath = 'images/highscores.png'
        img = py.image.load(imagePath).convert()
        config.screen.blit(img, (0, 0))
        py.display.flip()

        self.i = 0

        lista = []

        for x in self.file:
            if os.stat("highscores.txt").st_size == 0:
                break
            if x == '':
                self.file.remove(x)
                continue
            x = int(x)
            lista.append(x)
        lista.sort()
        lista.reverse()

        for line in lista[:5]:
            line = str(line)
            text = config.font.render(line, True, (255, 245, 1), (81, 81, 81))
            textRect = text.get_rect()
            textRect.center = (300, 390 + self.i)
            self.i += 50

            config.screen.blit(text, textRect)
            py.display.update()

        while self.running:

            for events in py.event.get():
                if events.type == py.KEYDOWN:
                    if events.key == py.K_RETURN:
                        h = titlescreen.Titlescreen()
                        self.running = False

    def addScore(self, score):
        self.file.write(str(score) + "\n")

    def displayScore(self):
        py.init()
        config.screen

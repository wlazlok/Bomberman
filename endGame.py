import config, pygame as py, play, titlescreen


class EndGame:
    def __init__(self):
        config.actual_level = 1
        py.display.set_mode((1024, 768))
        config.clearBackground()
        config.screen.blit(config.again, (0, 0))

        self.running = True

        self.button_choosen_id = 0
        self.button_choosen = {0: 'images/again.png', 1: 'images/do_menu.png'}

        img = py.image.load('images/again.png').convert()
        config.screen.blit(img, (0, 0))
        py.display.flip()


        while self.running:
            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_DOWN:
                        self.button_choosen_id += 1
                        if self.button_choosen_id == 2:
                            self.button_choosen_id -= 2
                        imagePath = self.button_choosen[self.button_choosen_id]
                        img = py.image.load(imagePath).convert()
                        config.screen.blit(img, (0, 0))
                        py.display.flip()
                        py.display.update()

                    if event.key == py.K_UP:
                        self.button_choosen_id -= 1
                        if self.button_choosen_id < 0:
                            self.button_choosen_id += 2
                        imagePath = self.button_choosen[self.button_choosen_id]
                        img = py.image.load(imagePath).convert()
                        config.screen.blit(img, (0, 0))
                        py.display.flip()
                        py.display.update()

                    if event.key == py.K_RETURN:
                        if self.button_choosen_id == 0:
                            play.Play(1)
                            self.running = False

                        if self.button_choosen_id == 1:
                            py.mixer.init()
                            py.mixer.music.load('sounds/title.wav')
                            py.mixer.music.play(-1)
                            py.mixer.music.set_volume(config.volume)
                            titlescreen.Titlescreen()
                            self.running = False




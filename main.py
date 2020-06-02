from titlescreen import Titlescreen
from pygame import mixer


mixer.init()
mixer.music.load('sounds/title.wav')
mixer.music.play(-1)
mixer.music.set_volume(1)
m = Titlescreen()




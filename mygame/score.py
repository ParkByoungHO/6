from pico2d import *
import showdownnote
import minus1note
import main_state

class score:
    def __init__(self):
        self.coolcount = 0
        self.goodcount = 0
        self.failcount = 0
        self.combocount = 0



    def draw(self):
        print('cool : %d' % self.coolcount)
        print('good : %d' % self.goodcount)
        print('fail : %d' % self.failcount)
        print('combo: %d' % self.combocount)


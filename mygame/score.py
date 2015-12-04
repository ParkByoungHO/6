import game_framework
import title_state
import json
from pico2d import *

name = "score"

class Score():
    def __init__(self,student_l):
        self.cool = student_l[0]
        self.good = student_l[1]
        self.fail = student_l[2]
        self.score = student_l[3]
    def draw(self):
        font.draw( 350, 350,'%s' %(self.cool),(255,125,0))
        font.draw( 350, 300,'%s' %(self.good),(255,125,0))
        font.draw( 350, 250,'%s' %(self.fail),(255,125,0))
        font.draw( 350, 200,'%s' %(self.score),(255,125,0))


def enter():
    global image,font,s
    image = load_image('resource/blue.png')
    font = load_font('resource/Moebius.ttf',30)

    f = open('resource/Score.txt','r').read().split() #텍스트파일에서 정보를 읽어와서 공백을 기준으로 나눔.
    s = Score(f) #그 정보를 student클래스의 생성자 인자로 보냄.

def exit():
    global image,font,s
    del(image)
    del(font)


    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN,SDLK_RETURN):
                game_framework.change_state(title_state)

def draw(frame_time):
    global image,s
    clear_canvas()
    image.draw(400, 300,800,600)
    s.draw()
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass





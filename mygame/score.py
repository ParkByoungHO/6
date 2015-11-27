import game_framework
import state
import say_that_you_note
import title_state
import showdown
import minus1note
from pico2d import *



name = "score"
image = None


def enter():
    global image,cool,good,fail,combo
    image = load_image('resource/blackbg.jpg')
    cool = minus1note.State.cool()
    good = minus1note.State.good()
    fail = minus1note.State.fail()
    combo =minus1note.State.combo()


def exit():
    global image,cool,good,fail,combo
    del(image)
    del(cool)
    del(good)
    del(fail)
    del(combo)

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


    pass


def draw(frame_time):
    clear_canvas()
    image.draw(400,300,800,600)
    print(cool,good,fail,combo)
    update_canvas()
    pass







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass





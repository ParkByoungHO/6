import game_framework
import title_state

from pico2d import *

name = "StartState"
image = None


def enter():
    global image,bgm
    open_canvas(sync=True)
    image = load_image('resource/bg.png')
    bgm = load_music('resource/1.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()
    pass


def exit():
    global image,bgm
    del(image)
    del(bgm)
    close_canvas()
    pass


def update(frame_time):

    pass


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400,300,800,600)
    update_canvas()
    pass




def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            bgm.set_volume(0)
            game_framework.push_state(title_state)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass


def pause(): pass


def resume(): pass





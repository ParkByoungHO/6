import game_framework
import main_state
import title_state
import jam
from pico2d import *
import showdownnote


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('resource/mpolice.jpg')
    pass


def exit():
    global image
    del(image)

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
                game_framework.change_state(showdownnote)
            elif(event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
                game_framework.change_state(title_state)
            elif(event.type, event.key) == (SDL_KEYDOWN,SDLK_LEFT):
                game_framework.change_state(jam)

    pass


def draw(frame_time):
    clear_canvas()
    image.draw(400,300,800,600)
    update_canvas()
    pass







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass





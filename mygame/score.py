import game_framework
import title_state
import json
from pico2d import *



name = "score"



def enter():
    global image,font
    image = load_image('resource/blue.png')
    font = load_font('resource/Moebius.ttf',30)


def exit():
    global image,font
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


def draw_score():
    with open('resource/Score.txt', 'r') as f:
        score_list = json.load(f)
    font.draw(300, 500, '[SCORE]', (255,255,255))
    for i, record in enumerate(score_list):
        font.draw(20, 450, '(cool:%4.1d, good:%4.1d,failcount:4.1d, COMBO:%3d, score:%4.1d)' % ('cool','good','fail','score','combo'), (255,255,255))



def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)

    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass





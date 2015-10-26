import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"
class Fkey:

    PIXEL_PER_METER = (10.0 / 0.1) #10 pixel 10cm
    NOTE_SPEED_KMPH = 4.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 20,random.randint(600,21000)
        self.total_frames = 0.0
        self.dir = -1
        self.frame = 0
        if Fkey.image == None:
            Fkey.image = load_image('resource/green_note.png')


    def draw(self):
        self.image.clip_draw(self.frame*40,0,40,10,self.x,self.y)

    def update(self,frame_time):
        self.frame=int(self.total_frames)%5
        distance = self.NOTE_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.total_frames += 1.0
        self.framerame = int(self.total_frames) % 2
        self.y += (self.dir*distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 5, self.x + 20, self.y + 5
    def handle_events(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS * 2.0
            self.y *= 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS / 2.0
            self.y /= 2



class Tkey:

    PIXEL_PER_METER = (10.0 / 0.1) #10 pixel 10cm
    NOTE_SPEED_KMPH = 4.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 60,random.randint(600,21000)
        self.total_frames = 0.0
        self.dir = -1
        self.frame = 0
        if Tkey.image == None:
            Tkey.image = load_image('resource/sky_note.png')


    def draw(self):
        self.image.clip_draw(self.frame*40,0,40,10,self.x,self.y)

    def update(self,frame_time):
        self.frame=int(self.total_frames)%5
        distance = self.NOTE_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.total_frames += 1.0
        self.framerame = int(self.total_frames) % 2
        self.y += (self.dir*distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 5, self.x + 20, self.y + 5
    def handle_events(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS * 2.0
            self.y *= 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS / 2.0
            self.y /= 2
class Hkey:

    PIXEL_PER_METER = (10.0 / 0.1) #10 pixel 10cm
    NOTE_SPEED_KMPH = 4.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 100,random.randint(600,21000)
        self.total_frames = 0.0
        self.dir = -1
        self.frame = 0
        if Hkey.image == None:
            Hkey.image = load_image('resource/green_note.png')


    def draw(self):
        self.image.clip_draw(self.frame*40,0,40,10,self.x,self.y)

    def update(self,frame_time):
        self.frame=int(self.total_frames)%5
        distance = self.NOTE_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.total_frames += 1.0
        self.framerame = int(self.total_frames) % 2
        self.y += (self.dir*distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 5, self.x + 20, self.y + 5
    def handle_events(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS * 2.0
            self.y *= 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS / 2.0
            self.y /= 2
class Ukey:

    PIXEL_PER_METER = (10.0 / 0.1) #10 pixel 10cm
    NOTE_SPEED_KMPH = 4.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 140,random.randint(600,21000)
        self.total_frames = 0.0
        self.dir = -1
        self.frame = 0
        if Ukey.image == None:
            Ukey.image = load_image('resource/sky_note.png')


    def draw(self):
        self.image.clip_draw(self.frame*40,0,40,10,self.x,self.y)

    def update(self,frame_time):
        self.frame=int(self.total_frames)%5
        distance = self.NOTE_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.total_frames += 1.0
        self.framerame = int(self.total_frames) % 2
        self.y += (self.dir*distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 5, self.x + 20, self.y + 5
    def handle_events(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS * 2.0
            self.y *= 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS / 2.0
            self.y /= 2
class Kkey:

    PIXEL_PER_METER = (10.0 / 0.1) #10 pixel 10cm
    NOTE_SPEED_KMPH = 4.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 180,random.randint(600,21000)
        self.total_frames = 0.0
        self.dir = -1
        self.frame = 0
        if Kkey.image == None:
            Kkey.image = load_image('resource/sky_note.png')


    def draw(self):
        self.image.clip_draw(self.frame*40,0,40,10,self.x,self.y)

    def update(self,frame_time):
        self.frame=int(self.total_frames)%5
        distance = self.NOTE_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.total_frames += 1.0
        self.framerame = int(self.total_frames) % 2
        self.y += (self.dir*distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 5, self.x + 20, self.y + 5
    def handle_events(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS * 2.0
            self.y *= 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.NOTE_SPEED_PPS = self.NOTE_SPEED_PPS / 2.0
            self.y /= 2



def enter():
    global sound,fkey,tkey,hkey,ukey,kkey
    fkey = [Fkey() for i in range(50)]
    tkey = [Tkey() for i in range(50)]
    hkey = [Hkey() for i in range(50)]
    ukey = [Ukey() for i in range(50)]
    kkey = [Kkey() for i in range(50)]
    sound =load_music('resource/say that you.mp3')
    sound.set_volume(64)
    sound.play(1)
    pass


def exit():
    global sound,fkey,tkey,hkey,ukey,kkey
    del(fkey)
    del(sound)
    del(tkey)
    del(hkey)
    del(ukey)
    del(kkey)
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            game_framework.change_state(title_state)
    pass


def update(frame_time):
    for F in fkey:
        F.update(frame_time)
    for T in tkey:
        T.update(frame_time)
    for H in hkey:
        H.update(frame_time)
    for U in ukey:
        U.update(frame_time)
    for K in kkey:
        K.update(frame_time)
    pass


def draw(frame_time):
    global running
    running = True
    while running:
        handle_events(frame_time)
        for T in tkey:
            T.update(frame_time)
        for F in fkey:
            F.update(frame_time)
        for H in hkey:
            H.update(frame_time)
        for U in ukey:
            U.update(frame_time)
        for K in kkey:
            K.update(frame_time)
        clear_canvas()
        for T in tkey:
            T.draw()
        for F in fkey:
            F.draw()
        for H in hkey:
            H.draw()
        for U in ukey:
            U.draw()
        for K in kkey:
            K.draw()

        delay(frame_time*0.0001)
        update_canvas()

    close_canvas()
    pass






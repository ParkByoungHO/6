import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"
class Fkey:

    PIXEL_PER_METER = (10.0 / 0.1) #10 pixel 10cm
    NOTE_SPEED_KMPH = 20.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 45,600
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
    NOTE_SPEED_KMPH = 20.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 90,600
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
    NOTE_SPEED_KMPH = 20.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 140,600
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
    NOTE_SPEED_KMPH = 20.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 188,600
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
    NOTE_SPEED_KMPH = 20.0          # K, / Hour
    NOTE_SPEED_MPM = (NOTE_SPEED_KMPH*1000.0 / 60.0)
    NOTE_SPEED_MPS = (NOTE_SPEED_MPM / 60.0)
    NOTE_SPEED_PPS = (NOTE_SPEED_MPS * PIXEL_PER_METER)
    # 1pixel / sec = 0.00305833945

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    image = None
    def __init__(self):
        self.x , self.y = 230,600
        self.total_frames = 0.0
        self.dir = -1
        self.frame = 0
        if Kkey.image == None:
            Kkey.image = load_image('resource/green_note.png')


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
    global bgimage, button,motionF,motionT,motionH,motionU,motionK
    motionF = load_image('resource/keyboard_motion_green.png')
    motionT= load_image('resource/keyboard_motion_sky.png')
    motionH= load_image('resource/keyboard_motion_green.png')
    motionU= load_image('resource/keyboard_motion_sky.png')
    motionK= load_image('resource/keyboard_motion_green.png')
    bgimage = load_image('resource/blackbg.jpg')
    button = load_image('resource/button.png')
    global green,blue
    global state
    global fkey,f1key,f2key,f3key,f4key,f5key,f6key,f7key,f8key,f9key,f10key,f11key,f12key,f13key,f14key,f15key
    global f16key,f17key,f18key,f19key,f20key,f21key,f22key,f23key,f24key,f25key,f26key,f27key,f28key,f29key,f30key
    global tkey,t1key,t2key,t3key,t4key,t5key,t6key,t7key,t8key,t9key,t10key,t11key,t12key,t13key,t14key,t15key
    global t16key,t17key,t18key,t19key,t20key,t21key,t22key,t23key,t24key,t25key,t26key,t27key,t28key,t29key,t30key
    global t31key
    global hkey,h1key,h2key,h3key,h4key,h5key,h6key,h7key,h8key,h9key,h10key,h11key,h12key,h13key,h14key,h15key
    global h16key,h17key,h18key,h19key,h20key,h21key,h22key,h23key,h24key,h25key,h26key,h27key,h28key,h29key,h30key
    global ukey,u1key,u2key,u3key,u4key,u5key,u6key,u7key,u8key,u9key,u10key,u11key,u12key,u13key,u14key,u15key
    global u16key,u17key,u18key,u19key,u20key,u21key,u22key,u23key,u24key,u25key,u26key,u27key,u28key,u29key,u30key
    global kkey,k1key,k2key,k3key,k4key,k5key,k6key,k7key,k8key,k9key,k10key,k11key,k12key,k13key,k14key,k15key
    global k16key,k17key,k18key,k19key,k20key,k21key,k22key,k23key,k24key,k25key,k26key,k27key,k28key,k29key,k30key
    global sound
    fkey = Fkey()
    f1key = Fkey()
    f2key = Fkey()
    f3key = Fkey()
    f4key = Fkey()
    f5key = Fkey()
    f6key = Fkey()
    f7key = Fkey()
    f8key = Fkey()
    f9key = Fkey()
    f10key = Fkey()
    f11key = Fkey()
    f12key = Fkey()
    f13key = Fkey()
    f14key = Fkey()
    f15key = Fkey()
    f16key = Fkey()
    f17key = Fkey()
    f18key = Fkey()
    f19key = Fkey()
    f20key = Fkey()
    f21key = Fkey()
    f22key = Fkey()
    f23key = Fkey()
    f24key = Fkey()
    f25key = Fkey()
    f26key = Fkey()
    f27key = Fkey()
    f28key = Fkey()
    f29key = Fkey()
    f30key = Fkey()
    tkey = Tkey()
    t1key = Tkey()
    t2key = Tkey()
    t3key = Tkey()
    t4key = Tkey()
    t5key = Tkey()
    t6key = Tkey()
    t7key = Tkey()
    t8key = Tkey()
    t9key = Tkey()
    t10key = Tkey()
    t11key = Tkey()
    t12key = Tkey()
    t13key = Tkey()
    t14key = Tkey()
    t15key = Tkey()
    t16key = Tkey()
    t17key = Tkey()
    t18key = Tkey()
    t19key = Tkey()
    t20key = Tkey()
    t21key = Tkey()
    t22key = Tkey()
    t23key = Tkey()
    t24key = Tkey()
    t25key = Tkey()
    t26key = Tkey()
    t27key = Tkey()
    t28key = Tkey()
    t29key = Tkey()
    t30key = Tkey()
    t31key = Tkey()
    hkey = Hkey()
    h1key = Hkey()
    h2key = Hkey()
    h3key = Hkey()
    h4key = Hkey()
    h5key = Hkey()
    h6key = Hkey()
    h7key = Hkey()
    h8key = Hkey()
    h9key = Hkey()
    h10key = Hkey()
    h11key = Hkey()
    h12key = Hkey()
    h13key = Hkey()
    h14key = Hkey()
    h15key = Hkey()
    h16key = Hkey()
    h17key = Hkey()
    h18key = Hkey()
    h19key = Hkey()
    h20key = Hkey()
    h21key = Hkey()
    h22key = Hkey()
    h23key = Hkey()
    h24key = Hkey()
    h25key = Hkey()
    h26key = Hkey()
    h27key = Hkey()
    h28key = Hkey()
    h29key = Hkey()
    h30key = Hkey()
    ukey = Ukey()
    u1key = Ukey()
    u2key = Ukey()
    u3key = Ukey()
    u4key = Ukey()
    u5key = Ukey()
    u6key = Ukey()
    u7key = Ukey()
    u8key = Ukey()
    u9key = Ukey()
    u10key = Ukey()
    u11key = Ukey()
    u12key = Ukey()
    u13key = Ukey()
    u14key = Ukey()
    u15key = Ukey()
    u16key = Ukey()
    u17key = Ukey()
    u18key = Ukey()
    u19key = Ukey()
    u20key = Ukey()
    u21key = Ukey()
    u22key = Ukey()
    u23key = Ukey()
    u24key = Ukey()
    u25key = Ukey()
    u26key = Ukey()
    u27key = Ukey()
    u28key = Ukey()
    u29key = Ukey()
    u30key = Ukey()
    kkey = Kkey()
    k1key = Kkey()
    k2key = Kkey()
    k3key = Kkey()
    k4key = Kkey()
    k5key = Kkey()
    k6key = Kkey()
    k7key = Kkey()
    k8key = Kkey()
    k9key = Kkey()
    k10key = Kkey()
    k11key = Kkey()
    k12key = Kkey()
    k13key = Kkey()
    k14key = Kkey()
    k15key = Kkey()
    k16key = Kkey()
    k17key = Kkey()
    k18key = Kkey()
    k19key = Kkey()
    k20key = Kkey()
    k21key = Kkey()
    k22key = Kkey()
    k23key = Kkey()
    k24key = Kkey()
    k25key = Kkey()
    k26key = Kkey()
    k27key = Kkey()
    k28key = Kkey()
    k29key = Kkey()
    k30key = Kkey()

    sound =load_music('resource/say that you.mp3')
    sound.set_volume(64)
    sound.play(1)
    pass


def exit():
    global bgimage,buttonn,motionF,motionT,motionH,motionU,motionK
    global green,blue
    global state
    del(bgimage,button,motionF,motionT,motionH,motionU,motionK)
    del(green,blue)
    global fkey,f1key,f2key,f3key,f4key,f5key,f6key,f7key,f8key,f9key,f10key,f11key,f12key,f13key,f14key,f15key
    global f16key,f17key,f18key,f19key,f20key,f21key,f22key,f23key,f24key,f25key,f26key,f27key,f28key,f29key,f30key
    global tkey,t1key,t2key,t3key,t4key,t5key,t6key,t7key,t8key,t9key,t10key,t11key,t12key,t13key,t14key,t15key
    global t16key,t17key,t18key,t19key,t20key,t21key,t22key,t23key,t24key,t25key,t26key,t27key,t28key,t29key,t30key
    global t31key
    global hkey,h1key,h2key,h3key,h4key,h5key,h6key,h7key,h8key,h9key,h10key,h11key,h12key,h13key,h14key,h15key
    global h16key,h17key,h18key,h19key,h20key,h21key,h22key,h23key,h24key,h25key,h26key,h27key,h28key,h29key,h30key
    global ukey,u1key,u2key,u3key,u4key,u5key,u6key,u7key,u8key,u9key,u10key,u11key,u12key,u13key,u14key,u15key
    global u16key,u17key,u18key,u19key,u20key,u21key,u22key,u23key,u24key,u25key,u26key,u27key,u28key,u29key,u30key
    global kkey,k1key,k2key,k3key,k4key,k5key,k6key,k7key,k8key,k9key,k10key,k11key,k12key,k13key,k14key,k15key
    global k16key,k17key,k18key,k19key,k20key,k21key,k22key,k23key,k24key,k25key,k26key,k27key,k28key,k29key,k30key
    global sound
    del(fkey,f1key,f2key,f3key,f4key,f5key,f6key,f7key,f8key,f9key,f10key,f11key,f12key,f13key,f14key,f15key)
    del(f16key,f17key,f18key,f19key,f20key,f21key,f22key,f23key,f24key,f25key,f26key,f27key,f28key,f29key,f30key)
    del(tkey,t1key,t2key,t3key,t4key,t5key,t6key,t7key,t8key,t9key,t10key,t11key,t12key,t13key,t14key,t15key)
    del(t16key,t17key,t18key,t19key,t20key,t21key,t22key,t23key,t24key,t25key,t26key,t27key,t28key,t29key,t30key)
    del(t31key,)
    del(hkey,h1key,h2key,h3key,h4key,h5key,h6key,h7key,h8key,h9key,h10key,h11key,h12key,h13key,h14key,h15key)
    del(h16key,h17key,h18key,h19key,h20key,h21key,h22key,h23key,h24key,h25key,h26key,h27key,h28key,h29key,h30key)
    del(ukey,u1key,u2key,u3key,u4key,u5key,u6key,u7key,u8key,u9key,u10key,u11key,u12key,u13key,u14key,u15key)
    del(u16key,u17key,u18key,u19key,u20key,u21key,u22key,u23key,u24key,u25key,u26key,u27key,u28key,u29key,u30key)
    del(kkey,k1key,k2key,k3key,k4key,k5key,k6key,k7key,k8key,k9key,k10key,k11key,k12key,k13key,k14key,k15key)
    del( k16key,k17key,k18key,k19key,k20key,k21key,k22key,k23key,k24key,k25key,k26key,k27key,k28key,k29key,k30key)
    del(sound)
    pass


def pause():
    pass


def resume():
    pass
def Fkey_update(frame_time):

    fkey.update(frame_time), f1key.update(frame_time), f2key.update(frame_time), f3key.update(frame_time), f4key.update(frame_time), f5key.update(frame_time), f6key.update(frame_time)
    f7key.update(frame_time),f8key.update(frame_time),f9key.update(frame_time),f10key.update(frame_time),f11key.update(frame_time),f12key.update(frame_time),f13key.update(frame_time),f30key.update(frame_time)
    f14key.update(frame_time),f15key.update(frame_time),f16key.update(frame_time),f17key.update(frame_time),f18key.update(frame_time),f19key.update(frame_time),f20key.update(frame_time),f21key.update(frame_time)
    f22key.update(frame_time),f23key.update(frame_time),f24key.update(frame_time),f25key.update(frame_time),f26key.update(frame_time),f27key.update(frame_time),f28key.update(frame_time),f29key.update(frame_time),
def Tkey_update(frame_time):
    tkey.update(frame_time), t1key.update(frame_time), t2key.update(frame_time), t3key.update(frame_time), t4key.update(frame_time), t5key.update(frame_time), t6key.update(frame_time)
    t7key.update(frame_time),t8key.update(frame_time),t9key.update(frame_time),t10key.update(frame_time),t11key.update(frame_time),t12key.update(frame_time),t13key.update(frame_time),t30key.update(frame_time)
    t14key.update(frame_time),t15key.update(frame_time),t16key.update(frame_time),t17key.update(frame_time),t18key.update(frame_time),t19key.update(frame_time),t20key.update(frame_time),t21key.update(frame_time)
    t22key.update(frame_time),t23key.update(frame_time),t24key.update(frame_time),t25key.update(frame_time),t26key.update(frame_time),t27key.update(frame_time),t28key.update(frame_time),t29key.update(frame_time),
    t31key.update(frame_time)
def Hkey_update(frame_time):
    hkey.update(frame_time), h1key.update(frame_time), h2key.update(frame_time), h3key.update(frame_time), h4key.update(frame_time), h5key.update(frame_time), h6key.update(frame_time)
    h7key.update(frame_time),h8key.update(frame_time),h9key.update(frame_time),h10key.update(frame_time),h11key.update(frame_time),h12key.update(frame_time),h13key.update(frame_time),h30key.update(frame_time)
    h14key.update(frame_time),h15key.update(frame_time),h16key.update(frame_time),h17key.update(frame_time),h18key.update(frame_time),h19key.update(frame_time),h20key.update(frame_time),h21key.update(frame_time)
    h22key.update(frame_time),h23key.update(frame_time),h24key.update(frame_time),h25key.update(frame_time),h26key.update(frame_time),h27key.update(frame_time),h28key.update(frame_time),h29key.update(frame_time),
def Ukey_update(frame_time):
    ukey.update(frame_time), u1key.update(frame_time), u2key.update(frame_time), u3key.update(frame_time), u4key.update(frame_time), u5key.update(frame_time), u6key.update(frame_time)
    u7key.update(frame_time),u8key.update(frame_time),u9key.update(frame_time),u10key.update(frame_time),u11key.update(frame_time),u12key.update(frame_time),u13key.update(frame_time),u30key.update(frame_time)
    u14key.update(frame_time),u15key.update(frame_time),u16key.update(frame_time),u17key.update(frame_time),u18key.update(frame_time),u19key.update(frame_time),u20key.update(frame_time),u21key.update(frame_time)
    u22key.update(frame_time),u23key.update(frame_time),u24key.update(frame_time),u25key.update(frame_time),u26key.update(frame_time),u27key.update(frame_time),u28key.update(frame_time),u29key.update(frame_time),
def Kkey_update(frame_time):
    kkey.update(frame_time), k1key.update(frame_time), k2key.update(frame_time), k3key.update(frame_time), k4key.update(frame_time), k5key.update(frame_time), k6key.update(frame_time)
    k7key.update(frame_time),k8key.update(frame_time),k9key.update(frame_time),k10key.update(frame_time),k11key.update(frame_time),k12key.update(frame_time),k13key.update(frame_time),k30key.update(frame_time)
    k14key.update(frame_time),k15key.update(frame_time),k16key.update(frame_time),k17key.update(frame_time),k18key.update(frame_time),k19key.update(frame_time),k20key.update(frame_time),k21key.update(frame_time)
    k22key.update(frame_time),k23key.update(frame_time),k24key.update(frame_time),k25key.update(frame_time),k26key.update(frame_time),k27key.update(frame_time),k28key.update(frame_time),k29key.update(frame_time),
def handle_events(frame_time):
    events = get_events()
    global green,blue,state
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f :
            state = 1
            green = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h :
            state = 2
            green = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_k :
            state = 3
            green = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_t :
            state = 4
            blue = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_u :
            state = 5
            blue = True

        elif event.type == SDL_KEYUP and event.key == SDLK_f :
            state = 0
            green = False
        elif event.type == SDL_KEYUP and event.key == SDLK_h :
            state = 0
            green = False
        elif event.type == SDL_KEYUP and event.key == SDLK_k :
            state = 0
            green = False
        elif event.type == SDL_KEYUP and event.key == SDLK_t :
            state = 0
            blue = False
        elif event.type == SDL_KEYUP and event.key == SDLK_u :
            state = 0
            blue = False
    pass



def update(frame_time):
    Fkey_update(frame_time)
    Tkey_update(frame_time)
    Hkey_update(frame_time)
    Ukey_update(frame_time)
    Kkey_update(frame_time)

    pass
def nodeupdate(frame_time): #노트 나오게한다.
    if a >= 0.5:
        fkey.update(frame_time)
        fkey.draw()
    if a >= 0.75:
        tkey.update(frame_time)
        tkey.draw()
    if a>= 1.1:
        kkey.update(frame_time)
        kkey.draw()
    if a>= 2:
        k1key.update(frame_time)
        k1key.draw()
    if a>=2.4:
        f1key.update(frame_time)
        f1key.draw()
    if a >=3.800: #동시 두개
        f2key.update(frame_time)
        f2key.draw()
        ukey.update(frame_time)
        ukey.draw()
    if a>=4.000: #동시 두개
        f3key.update(frame_time)
        f3key.draw()
        hkey.update(frame_time)
        hkey.draw()
    if a>=4.300:
        t1key.update(frame_time)
        t1key.draw()
    if a>= 4.750:
        t2key.update(frame_time)
        t2key.draw()
    if a>= 5.100:
        t3key.update(frame_time)
        t3key.draw()
    if a>= 5.600: # 두개
        k3key.update(frame_time)
        k3key.draw()
        h2key.update(frame_time)
        h2key.draw()

    if a>= 7.000: # 두개
        f4key.update(frame_time)
        f4key.draw()
        t4key.update(frame_time)
        t4key.draw()
    if a>=7.200:
        f5key.update(frame_time)
        f5key.draw()

    if a>=9.600:
        u1key.update(frame_time)
        u1key.draw()

    if a>= 10.500:
        t5key.update(frame_time)
        t5key.draw()
        u2key.update(frame_time)
        u2key.draw()
    if a>= 11.000:
        f6key.update(frame_time)
        f6key.draw()
        k4key.update(frame_time)
        k4key.draw()

    if a>= 11.500:
        f7key.update(frame_time)
        f7key.draw()
        k5key.update(frame_time)
        k5key.draw()

    if a>= 12.100:
        h3key.update(frame_time)
        h3key.draw()
    if a>= 12.200:
        h4key.update(frame_time)
        h4key.draw()
    if a>= 12.300:
        h5key.update(frame_time)
        h5key.draw()
    if a>= 12.400:
        h6key.update(frame_time)
        h6key.draw()
    if a>= 13.000:
        u3key.update(frame_time)
        u3key.draw()
    if a>= 13.100:
        u4key.update(frame_time)
        u4key.draw()
    if a>= 13.200:
        u5key.update(frame_time)
        u5key.draw()
    if a>= 13.300:
        u6key.update(frame_time)
        u6key.draw()
    if a>= 13.600:
        k6key.update(frame_time)
        k6key.draw()
    if a>= 13.900:
        k7key.update(frame_time)
        k7key.draw()
    if a>= 14.200:
        k8key.update(frame_time)
        k8key.draw()

    if a>=15.300:
        h7key.update(frame_time)
        h7key.draw()
    if a>=15.400:
        h8key.update(frame_time)
        h8key.draw()
    if a>=15.500:
        h9key.update(frame_time)
        h9key.draw()
    if a>=15.600:
        h10key.update(frame_time)
        h10key.draw()
    if a>=16.200:
        t6key.update(frame_time)
        t6key.draw()
    if a>=16.300:
        t7key.update(frame_time)
        t7key.draw()
    if a>= 16.400:
        t8key.update(frame_time)
        t8key.draw()
    if a>= 16.500:
        t9key.update(frame_time)
        t9key.draw()
    if a>=16.800:
        f8key.update(frame_time)
        f8key.draw()
    if a>= 17.100:
        f9key.update(frame_time)
        f9key.draw()
    if a>= 17.400:
        f10key.update(frame_time)
        f10key.draw()

    if a>= 18.600:
        u7key.update(frame_time)
        u7key.draw()
    if a>=18.700:
        u8key.update(frame_time)
        u8key.draw()
    if a>=18.800:
        u9key.update(frame_time)
        u9key.draw()
    if a>=18.900:
        u10key.update(frame_time)
        u10key.draw()
    if a>=19.500:
        t10key.update(frame_time)
        t10key.draw()
    if a>=19.600:
        t11key.update(frame_time)
        t11key.draw()
    if a>=19.700:
        t12key.update(frame_time)
        t12key.draw()
    if a>=19.800:
        t13key.update(frame_time)
        t13key.draw()
    if a>=20.100:
        f11key.update(frame_time)
        f11key.draw()
    if a>=20.400:
        f12key.update(frame_time)
        f12key.draw()
    if a>=20.700:
        f13key.update(frame_time)
        f13key.draw()

    if a>= 21.700: #두개
        k9key.update(frame_time)
        k9key.draw()
        u11key.update(frame_time)
        u11key.draw()
    if a>= 22.600:
        h11key.update(frame_time)
        h11key.draw()
        u12key.update(frame_time)
        u12key.draw()
    if a>= 23.500:
        h12key.update(frame_time)
        h12key.draw()
        t14key.update(frame_time)
        t14key.draw()

    if a>= 24.850: #두개
        k10key.update(frame_time)
        k10key.draw()
        u13key.update(frame_time)
        u13key.draw()
    if a>= 25.750:
        h13key.update(frame_time)
        h13key.draw()
        u14key.update(frame_time)
        u14key.draw()
    if a>= 26.650:
        h14key.update(frame_time)
        h14key.draw()
        t15key.update(frame_time)
        t15key.draw()

    if a>= 28.300:
        h15key.update(frame_time)
        h15key.draw()
    if a>= 28.500:
        h16key.update(frame_time)
        h16key.draw()
    if a>= 28.700:
        h17key.update(frame_time)
        h17key.draw()
    if a>= 28.900:
        h18key.update(frame_time)
        h18key.draw()
    if a>= 29.100:
        h19key.update(frame_time)
        h19key.draw()
    if a>= 29.300:
        h20key.update(frame_time)
        h20key.draw()
    if a>= 29.500:
        h21key.update(frame_time)
        h21key.draw()
#
    if a>= 29.900:
        t16key.update(frame_time)
        t16key.draw()
    if a>= 30.200:
        u15key.update(frame_time)
        u15key.draw()
    if a>= 30.500:
        k11key.update(frame_time)
        k11key.draw()
    if a>= 29.800:
        f14key.update(frame_time)
        f14key.draw()
    if a>= 30.100:
        h22key.update(frame_time)
        h22key.draw()
    if a>= 30.400:
        f15key.update(frame_time)
        f15key.draw()
    if a>= 30.700:
        f16key.update(frame_time)
        f16key.draw()
    if a>= 31.000:
        k12key.update(frame_time)
        k12key.draw()
    if a>= 31.400:
        u16key.update(frame_time)
        u16key.draw()
    if a>= 31.800:
        u17key.update(frame_time)
        u17key.draw()
    if a>= 32.200:
        t17key.update(frame_time)
        t17key.draw()
    if a>= 32.600:
        t18key.update(frame_time)
        t18key.draw()
    if a>= 33.000:
        h23key.update(frame_time)
        h23key.draw()
    if a>= 33.400:
        f17key.update(frame_time)
        f17key.draw()
    if a>= 33.800:
        f18key.update(frame_time)
        f18key.draw()
    if a>= 34.200:
        h24key.update(frame_time)
        h24key.draw()
    if a>= 35.600:
        f20key.update(frame_time)
        f20key.draw()
    if a>= 35.900:
        f21key.update(frame_time)
        f21key.draw()
    if a>= 36.200:
        h26key.update(frame_time)
        h26key.draw()
    if a>= 36.500:
        t22key.update(frame_time)
        t22key.draw()
    if a>= 36.800:
        t23key.update(frame_time)
        t23key.draw()
    if a>= 37.100:
        k13key.update(frame_time)
        k13key.draw()
    if a>= 37.400:
        k14key.update(frame_time)
        k14key.draw()
    if a>= 37.700:
        u21key.update(frame_time)
        u21key.draw()
    if a>= 39.000:
        u22key.update(frame_time)
        u22key.draw()
    if a>= 39.300:
        f23key.update(frame_time)
        f23key.draw()
    if a>= 39.600:
        f24key.update(frame_time)
        f24key.draw()
    if a>= 39.900:
        h27key.update(frame_time)
        h27key.draw()
    if a>= 40.200:
        h28key.update(frame_time)
        h28key.draw()
    if a>= 40.500:
        u23key.update(frame_time)
        u23key.draw()

    if a>= 42.:  #
        f22key.update(frame_time)
        f22key.draw()
    if a>= 42.12:
        h25key.update(frame_time)
        h25key.draw()
    if a>= 42.24:
        u18key.update(frame_time)
        u18key.draw()
    if a>= 42.36:
        u19key.update(frame_time)
        u19key.draw()
    if a>= 42.48:
        f19key.update(frame_time)
        f19key.draw()
    if a>= 42.6:
        t19key.update(frame_time)
        t19key.draw()
    if a>= 42.72:
        t20key.update(frame_time)
        t20key.draw()
    if a>= 42.86:
        u20key.update(frame_time)
        u20key.draw()
        t21key.update(frame_time)
        t21key.draw()

    if a>= 44.55:
        k15key.update(frame_time)
        k15key.draw()
        f25key.update(frame_time)
        f25key.draw()
    if a>=46.5:
        k16key.update(frame_time)
        k16key.draw()
        t24key.update(frame_time)
        t24key.draw()

    if a>=48.0:
        u24key.update(frame_time)
        u24key.draw()
        t29key.update(frame_time)
        t29key.draw()

    if a>=49.0:
        k21key.update(frame_time)
        k21key.draw()
        f26key.update(frame_time)
        f26key.draw()

    if a>=49.8:
        k17key.update(frame_time)
        k17key.draw()
        t25key.update(frame_time)
        t25key.draw()
    if a>=50.1:
        k18key.update(frame_time)
        k18key.draw()
        t26key.update(frame_time)
        t26key.draw()
    if a>=50.4:
        k19key.update(frame_time)
        k19key.draw()
        t27key.update(frame_time)
        t27key.draw()
    if a>=50.7:
        k20key.update(frame_time)
        k20key.draw()
        t28key.update(frame_time)
        t28key.draw()













def draw(frame_time):
    global running
    running = True
    global a
    global green,blue,state
    green = blue = False
    a = 0
    while running:

        handle_events(frame_time)
        clear_canvas()
        bgimage.draw(400,300,800,600)
        nodeupdate(frame_time)
        if green == True and state ==1:
            motionF.draw(43,100,47,1000)
        if green == True and state ==2:
            motionH.draw(138,100,47,1000)
        if green == True and state ==3:
            motionK.draw(232,100,47,1000)
        if blue == True and state == 4:
            motionT.draw(90,100,47,1000)
        if blue == True  and state == 5:
            motionU.draw(185,100,47,1000)
        button.draw(200,100,400,200)
        update_canvas()
        a+=frame_time -0.000001
        print(a)


    close_canvas()
    pass






import random
import json
import os
import score
from pico2d import *

import game_framework
import title_state



name = "Jamnote"
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
        self.x , self.y = 45,random.randint(800,51800)
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
        self.x , self.y = 90,random.randint(800,51800)
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
        self.x , self.y = 140,random.randint(800,51800)
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
        self.x , self.y = 188,random.randint(800,51800)
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
        self.x , self.y = 230,random.randint(800,51800)
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
class buttontectangle:
    def __init__(self):
        self.x, self.y = 136,81.5
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-118,self.y-15.5,self.x+118,self.y+15.5

def soundplay(frame_time):

    global sound,soundmax
    soundmax = 100
    sound =load_music('resource/showdown.ogg')
    sound.set_volume(soundmax)
    sound.play(1)

class Cool:
    image = None
    def __init__(self):
        if Cool.image == None:
            Cool.image = load_image('resource/Cool.png')
        self.x,self.y = 340,300
        self.switch = False
    def draw(self):
        self.image.draw(self.x,self.y)

class Good:
    image = None
    def __init__(self):
        if Good.image == None:
            Good.image = load_image('resource/Good.png')
        self.x,self.y = 340,200
        self.switch = False
    def draw(self):
        self.image.draw(self.x,self.y)
class Fail:
    image = None
    def __init__(self):
        if Fail.image == None:
            Fail.image = load_image('resource/Fail.png')
        self.x,self.y = 340,100
        self.switch = False
    def draw(self):
        self.image.draw(self.x,self.y)
class Combo:
    image = None
    def __init__(self):
        if Combo.image == None:
            Combo.image = load_image('resource/combo.png')
        self.x,self.y = 320,400
    def draw(self):
        self.image.draw(self.x,self.y)







def enter():
    global bgimage, button,motionF,motionT,motionH,motionU,motionK,actbutton
    global Fkeynote,Tkeynote,Hkeynote,Ukeynote,Kkeynote,font,combo,combocount
    global green,blue,F,T,H,U,K
    global cool,good,fail
    global state
    motionF = load_image('resource/keyboard_motion_green.png')
    motionT= load_image('resource/keyboard_motion_sky.png')
    motionH= load_image('resource/keyboard_motion_green.png')
    motionU= load_image('resource/keyboard_motion_sky.png')
    motionK= load_image('resource/keyboard_motion_green.png')
    bgimage = load_image('resource/blackbg.jpg')
    button = load_image('resource/button.png')

    actbutton=buttontectangle()

    Fkeynote=[Fkey() for i in range (70)]
    Tkeynote=[Tkey() for o in range (70)]
    Hkeynote=[Hkey() for p in range (70)]
    Ukeynote=[Ukey() for u in range (70)]
    Kkeynote=[Kkey() for y in range (70)]
    cool = Cool()
    good = Good()
    fail = Fail()
    combo = Combo()
    font = load_font('resource/Moebius.TTF',30)
    pass


def exit():
    global bgimage,button,motionF,motionT,motionH,motionU,motionK,actbutton
    global Fkeynote,Tkeynote,Hkeynote,Ukeynote,Kkeynote,sound
    global green,blue
    global F,T,H,U,K
    global cool,good,fail,combo,combocount,font
    global state
    del(bgimage)
    del(button)
    del (motionF)
    del (motionT)
    del (motionH)
    del (motionU)
    del(motionK)
    del(actbutton)
    del(Fkeynote)
    del(Tkeynote)
    del(Hkeynote)
    del(Ukeynote)
    del(Kkeynote)
    del(green)
    del(blue)
    del(F)
    del(T)
    del(H)
    del(U)
    del(K)
    del(sound)
    del(cool)
    del(good)
    del(fail)
    del(font)
    del(combo)
    del(combocount)
    pass


def pause():
    pass


def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    global green,blue,state,running,F,T,H,U,K,example,sound
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()
            game_framework.run(title_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_f :
            F=True
            green = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h :
            H=True
            green = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_k :
            K=True
            green = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_t :
            T=True
            blue = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_u :
            U=True
            blue = True

        elif event.type == SDL_KEYUP and event.key == SDLK_f :
            F=False
            green = False
        elif event.type == SDL_KEYUP and event.key == SDLK_h :
            H=False
            green = False
        elif event.type == SDL_KEYUP and event.key == SDLK_k :
            K=False
            green = False
        elif event.type == SDL_KEYUP and event.key == SDLK_t :
            T=False
            blue = False
        elif event.type == SDL_KEYUP and event.key == SDLK_u :
            U=False
            blue = False
    pass

def coolcollide(a,b):#rectangle a  , note b
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if top_a-3 < bottom_b : return False
    if bottom_a+3 > top_b : return False
    return True

def goodcollide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

def misscollide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if top_b> bottom_a:return False
    return True

def update(frame_time):
    global Fkeynote,Tkeynote,Hkeynote,Ukeynote,Kkeynote
    global F,T,H,U,K,count
    F = T = H = U = K = False
    count = 0
    soundplay(frame_time)
def Timer(frame_time):
    global cool,good,fail,a
    if cool.switch:
        a+=frame_time
        if a>0.5:
            cool.switch = False
            a=0
    if good.switch:
        a+=frame_time
        if a>0.5:
            good.switch = False
            a=0
    if fail.switch:
        a+=frame_time
        if a>0.5:
            fail.switch = False
            a=0
def ranking():
    global coolcount,goodcount,failcount,sum

    score = (coolcount*10)+(goodcount*5)

    f= open("resource/Score.txt",'w')
    cool = "cool:%d   " % coolcount
    good = "good:%d   " % goodcount
    fail = "fail:%d   " % failcount
    Score = "score:%d " % score

    f.write(cool)
    f.write(good)
    f.write(fail)
    f.write(Score)

    f.close()


def draw(frame_time):
    global running
    running = True
    global a
    global Fkeynote,Tkeynote,Hkeynote,Ukeynote,Kkeynote,bgimage,actbutton,soundmax
    global green,blue,F,T,H,U,K
    global cool,good,fail,count,coolcount,goodcount,failcount,sum,combocount,font,combo
    global Score
    green = blue = F = T = H = U = K = False
    a = sum = coolcount=goodcount=failcount=sum=combocount=0
    count =0
    while running:
        handle_events(frame_time)

        for Fkeynotes in Fkeynote:
            Fkeynotes.update(frame_time)
        for Tkeynotes in Tkeynote:
            Tkeynotes.update(frame_time)
        for Hkeynotes in Hkeynote:
            Hkeynotes.update(frame_time)
        for Ukeynotes in Ukeynote:
            Ukeynotes.update(frame_time)
        for Kkeynotes in Kkeynote:
            Kkeynotes.update(frame_time)

        for Fkeynotes in Fkeynote:
            if F==True:
                if coolcollide(actbutton,Fkeynotes)==True:
                    Fkeynote.remove(Fkeynotes)
                    cool.switch=True
                    coolcount+=1
                    combocount+=1
                    sum+=1
                elif goodcollide(actbutton,Fkeynotes)==True:
                    Fkeynote.remove(Fkeynotes)
                    good.switch=True
                    goodcount+=1
                    combocount+=1
                    sum+=1
            if misscollide(actbutton,Fkeynotes):
                Fkeynote.remove(Fkeynotes)
                fail.switch=True
                failcount+=1
                combocount=0
        for Tkeynotes in Tkeynote:
            if T==True:
                if coolcollide(actbutton,Tkeynotes)==True:
                    Tkeynote.remove(Tkeynotes)
                    cool.switch=True
                    coolcount+=1
                    combocount+=1
                    sum+=1
                elif goodcollide(actbutton,Tkeynotes)==True:
                    Tkeynote.remove(Tkeynotes)
                    good.switch=True
                    goodcount+=1
                    combocount+=1
                    sum+=1
            if misscollide(actbutton,Tkeynotes):
                Tkeynote.remove(Tkeynotes)
                fail.switch=True
                failcount+=1
                combocount=0
        for Hkeynotes in Hkeynote:
            if H==True:
                if coolcollide(actbutton,Hkeynotes)==True:
                    Hkeynote.remove(Hkeynotes)
                    cool.switch=True
                    coolcount+=1
                    combocount+=1
                    sum+=1
                elif goodcollide(actbutton,Hkeynotes)==True:
                    Hkeynote.remove(Hkeynotes)
                    good.switch=True
                    goodcount+=1
                    combocount+=1
                    sum+=1
            if misscollide(actbutton,Hkeynotes):
                Hkeynote.remove(Hkeynotes)
                fail.switch=True
                failcount+=1
                combocount=0
        for Ukeynotes in Ukeynote:
            if U==True:
                if coolcollide(actbutton,Ukeynotes)==True:
                    Ukeynote.remove(Ukeynotes)
                    cool.switch=True
                    coolcount+=1
                    combocount+=1
                    sum+=1
                elif goodcollide(actbutton,Ukeynotes)==True:
                    Ukeynote.remove(Ukeynotes)
                    good.switch=True
                    goodcount+=1
                    combocount+=1
                    sum+=1
            if misscollide(actbutton,Ukeynotes):
                Ukeynote.remove(Ukeynotes)
                fail.switch=True
                failcount+=1
                combocount=0
        for Kkeynotes in Kkeynote:
            if K==True:
                if coolcollide(actbutton,Kkeynotes)==True:
                    Kkeynote.remove(Kkeynotes)
                    cool.switch=True
                    coolcount+=1
                    combocount+=1
                    sum+=1
                elif goodcollide(actbutton,Kkeynotes)==True:
                    Kkeynote.remove(Kkeynotes)
                    good.switch=True
                    goodcount+=1
                    combocount+=1
                    sum+=1
            if misscollide(actbutton,Kkeynotes):
                Kkeynote.remove(Kkeynotes)
                fail.switch=True
                failcount+=1
                combocount=0

        clear_canvas()
        bgimage.draw(400,300,800,600)
        for Fkeynotes in Fkeynote:
            Fkeynotes.draw()
        for Tkeynotes in Tkeynote:
            Tkeynotes.draw()
        for Hkeynotes in Hkeynote:
            Hkeynotes.draw()
        for Ukeynotes in Ukeynote:
            Ukeynotes.draw()
        for Kkeynotes in Kkeynote:
            Kkeynotes.draw()
        if green == True and F ==True:
            motionF.draw(43,100,47,1000)
        if green == True and H ==True:
            motionH.draw(138,100,47,1000)
        if green == True and K ==True:
            motionK.draw(232,100,47,1000)
        if blue == True and T ==True:
            motionT.draw(90,100,47,1000)
        if blue == True  and U ==True:
            motionU.draw(185,100,47,1000)
        if cool.switch:
            cool.draw()
            combo.draw()
            font.draw(312, 380, '%d' % (combocount), (255,125,0))
        if good.switch:
            good.draw()
            combo.draw()
            font.draw(312, 380, '%d' % (combocount), (255,125,0))
        if fail.switch:
            fail.draw()
        font.draw(312, 30, 'score : %d' % (coolcount*10+goodcount*5), (255,125,0))
        count+=frame_time
        Timer(frame_time)
        button.draw(200,100,400,200)
        update_canvas()
        if(count>97):
            ranking()
            exit()
            game_framework.run(score)





    close_canvas()


    pass






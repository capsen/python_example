import pgzrun
import pygame
from pgzhelper import *
from sprite import *

WIDTH = 800
HEIGHT = 600

show_elements=[]
current_frame=0

backdrop = Actor("arctic")
backdrop.topleft = (0, 0)
backdrop.images=["arctic", "baseball", "boardwalk"]
show_elements.append(backdrop)
backdrop.show=True

abby = Sprite("abby-a")
abby.topleft=(20, 280)
abby.scale=0.5

show_elements.append(abby)

devin = Sprite("devin-a")
devin.topleft=(620, 280)
devin.scale=0.5

show_elements.append(devin)

next_btn = Sprite("next_up")
next_btn.topleft=(520,500)
next_btn.scale=0.4
show_elements.append(next_btn)

prev_btn = Sprite("prev_up")
prev_btn.topleft=(100,500)
prev_btn.scale=0.4
show_elements.append(prev_btn)

def draw():
    screen.clear()
    for element in show_elements:
        if element.show :
            element.draw()

def frame_changed():
    match current_frame:
        case 0:
            abby.message=""
            devin.message=""
        case 1:
            abby.message="Hello how are you Kevin?"
            devin.message=""
        case 2:
            abby.message=""
            devin.message="I am good thanks and yourself?"
        case 3:
            abby.message="I am good thanks. Let's go out and play"
            devin.message=""
        case 4:
            abby.message=""
            devin.message="OK."
        case default:
            abby.message=""
            devin.message=""


def next_frame():
    global current_frame
    current_frame = current_frame + 1
    frame_changed()

def prev_frame():
    global current_frame
    current_frame = current_frame - 1
    frame_changed()

def update():
    # abby.screen = screen
    # devin.screen = screen
    pass
    

def on_mouse_down(pos):
    if next_btn.collidepoint(pos):
        # btn.image="clickdown"
        pass
    if prev_btn.collidepoint(pos):
        pass

def on_mouse_up(pos):
    if next_btn.collidepoint(pos):
        # btn.image="clickup"
        next_frame()
    if prev_btn.collidepoint(pos):
        prev_frame()

pgzrun.go() # Must be last line
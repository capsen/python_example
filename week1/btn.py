import pgzrun
import pygame
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

show_elements=[]
def showElement(element):
    global show_elements
    if not element in show_elements:
        show_elements.append(element)

def hideElement(element):
    global show_elements
    if element in show_elements:
        show_elements.remove(element)


backdrop = Actor("arctic")
backdrop.topleft = (0, 0)
backdrop.images=["arctic", "baseball", "boardwalk"]
showElement(backdrop)

btn = Actor("clickup")
btn.center=(400,300)
btn.scale=0.2
showElement(btn)

basketball = Actor("basketball")
showElement(basketball)

def draw():
    screen.clear()
    
    for element in show_elements:
        element.draw()

def update():
    pass

def btn_clicked():
    backdrop.animate()
    if basketball in show_elements:
        hideElement(basketball)
    else:
        showElement(basketball)

def on_mouse_down(pos):
    if btn.collidepoint(pos):
        btn.image="clickdown"

def on_mouse_up(pos):
    if btn.collidepoint(pos):
        btn.image="clickup"
        btn_clicked()
    if btn.image=="clickdown":
        btn.image="clickup"



pgzrun.go() # Must be last line
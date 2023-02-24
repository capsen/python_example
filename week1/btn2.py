import pgzrun
import pygame
from pgzhelper import *
from button import Button

WIDTH = 800
HEIGHT = 600

show_elements=[]
btns=[]
# def showElement(element):
#     global show_elements
#     if not element in show_elements:
#         show_elements.append(element)

# def hideElement(element):
#     global show_elements
#     if element in show_elements:
#         show_elements.remove(element)


backdrop = Actor("arctic")
backdrop.topleft = (0, 0)
backdrop.images=["arctic", "baseball", "boardwalk"]
show_elements.append(backdrop)
backdrop.show=True

btn = Actor("clickup")
btn.center=(400,300)
btn.scale=0.2
show_elements.append(btn)
btn.show=True

def btn1Click():
    print("btn1 clicked")
btn1 = Button("next",(200,200), callback=btn1Click)
btn1.scale=0.3
show_elements.append(btn1)
btns.append(btn1)

basketball = Actor("basketball")
basketball.show=True
show_elements.append(basketball)


def draw():
    screen.clear()
    
    for element in show_elements:
        if element.show :
            element.draw()
    screen.draw.text("All together now:\nCombining the above options",
        midbottom=(427,460), width=360, fontname="bauhs93", fontsize=12,
        color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
    screen.draw.text("Allow me to demonstrate wrapped text.", (90, 210), width=180, lineheight=1.5, background="gray")
    screen.draw.textbox("hello world Allow me to demonstrate wrapped text.", (100, 100, 200, 50), 
         background="white")

    color = (48, 141, 70)
    # Drawing Rectangle
    pygame.draw.rect(screen.surface, color, pygame.Rect(30, 30, 70, 70),  0, 0, 10, 10, 0, 10)
    pygame.draw.rect(screen.surface, (255,0,0), pygame.Rect(30, 30, 70, 70),  4, 0, 10, 10, 0, 10)
    screen.draw.textbox("hello world Allow me to demonstrate wrapped text.", (35, 35, 60, 60) )




def update():
    pass

def btn_clicked():
    backdrop.animate()
    if basketball.show :
        basketball.show=False
    else:
        basketball.show=True

def on_mouse_down(pos):
    for btnitem in btns:
        btnitem.on_mouse_down(pos)
    if btn.collidepoint(pos):
        btn.image="clickdown"

def on_mouse_up(pos):
    for btnitem in btns:
        btnitem.on_mouse_up(pos)
    if btn.collidepoint(pos):
        btn.image="clickup"
        btn_clicked()
    if btn.image=="clickdown":
        btn.image="clickup"



pgzrun.go() # Must be last line
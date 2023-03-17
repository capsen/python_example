import pgzrun
from pgzhelper import *
from sprite import *
from button import Button
from quizui import *

WIDTH = 800
HEIGHT = 600
elements = []
btns = []
current_frame=0

backdrops = Sprite("bg1")
backdrops.scale = 0.2
backdrops.pos=(400,300)

q = Option("option", pos=(400, 100), message="what's the answer of 1+3?")
q.scale = 2.5

question1 = {
    "description" : "What's the answer of 1+3?",
    "options" : [1, 2, 3, 4],
    "correct_answer" : 4
}

question2 = {
    "description" : "What's your favorite pet?",
    "options" : ["cat", "dog", "elephant", "snake"],
    "correct_answer" : 4
}

question_ui = Question()

question_ui.display_options(question1)

def draw():
    screen.clear()
    backdrops.draw()
    q.draw()
    question_ui.draw()

def on_mouse_down(pos):
        question_ui.on_mouse_down(pos)

def on_mouse_up(pos):
        question_ui.on_mouse_up(pos)

pgzrun.go()

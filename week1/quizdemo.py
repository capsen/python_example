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

question1 = {
    "description" : "What's the answer of 1+3?",
    "options" : [1, 2, 3, 4],
    "correct_answer" : 4
}

question2 = {
    "description" : "What's your favorite pet?",
    "options" : ["cat", "dog", "elephant", "snake"],
    "correct_answer" : "cat"
}

question3 = {
    "description" : "What's the distance between Mars and Sun",
    "options" : ["1AU", "3,000km", "1.5AU", "7million km"],
    "correct_answer" : "1.5AU"
}

questions = []
answers=[]
questions.append(question1)
questions.append(question2)
questions.append(question3)

current_question = 0



question_ui = Question(question=questions[current_question], select_callback=check_question)
question_ui.display_options(questions[current_question])

def draw():
    screen.clear()
    backdrops.draw()
    question_ui.draw()

def on_mouse_down(pos):
        question_ui.on_mouse_down(pos)

def on_mouse_up(pos):
        question_ui.on_mouse_up(pos)

pgzrun.go()

import pygame
import pgzrun
import json
from pgzhelper import *

mod = sys.modules['__main__']

class Option(Actor):
    def __init__(self, optionimage, optiontext, order="", pos=POS_TOPLEFT, callback=None, show=True):
        super().__init__(optionimage + '_up', pos)
        self.optionimage = optionimage
        self.callback = callback
        self.optiontext = optiontext
        self.show=show
        self.order=order

    def on_mouse_down(self, pos):
        if self.show and self.collidepoint(pos):
            self.image=self.optionimage + "_down"

    def on_mouse_up(self, pos):
        if self.show and self.collidepoint(pos):
            self.image=self.optionimage + "_up"
            if self.callback:
                self.callback(self.optiontext)

    def draw(self):
        if self.show:
            super().draw()
            self.drawtext()
    
    def drawtext(self):
        topleft=self.topleft
        x=topleft[0]
        y=topleft[1]
        mod.screen.draw.textbox(self.order+self.optiontext, (x+self.width/11, y+self.height/8, self.width-self.width/11*2, self.height-self.height/8*2))


class Question():
    def __init__(self, question, callback=None):
        self.question = question
        self.current_answer=None
        self.callback = callback
        self.questionUI = Option("question", question["description"], pos=(400, 200))
        self.questionUI.scale=0.6
        self.op1 = Option("option", str(question["options"][0]), order="A. ", callback=self.option_clicked, pos=(200, 400))
        self.op1.scale=0.4
        self.op2 = Option("option", str(question["options"][1]), order="B. ", callback=self.option_clicked, pos=(600, 400))
        self.op2.scale=0.4
        self.op3 = Option("option", str(question["options"][2]), order="C. ", callback=self.option_clicked, pos=(200, 480))
        self.op3.scale=0.4
        self.op4 = Option("option", str(question["options"][3]), order="D. ", callback=self.option_clicked, pos=(600, 480))
        self.op4.scale=0.4
        
    
    def option_clicked(self, option_value):
        self.current_answer=option_value
        print(option_value)
        self.slide([self.questionUI, self.op1, self.op2, self.op3, self.op4], 0.5, False)
        clock.schedule(self.callback, 0.5)
        

    def start_entry(self):
        self.slide([self.questionUI, self.op1, self.op2, self.op3, self.op4], 0.5, True)
    
    def slide(self, objs, duration, isEntry):
        for obj in objs:
            end=obj.pos if isEntry else (obj.pos[0]-800,obj.pos[1])
            start=(obj.pos[0]+800,obj.pos[1]) if isEntry else obj.pos
            obj.pos=start
            animate(obj, pos=end, duration=duration)
    
    def draw(self):
        self.questionUI.draw()
        self.op1.draw()
        self.op2.draw()
        self.op3.draw()
        self.op4.draw()
    
    def on_mouse_down(self, pos):
        self.op1.on_mouse_down(pos)
        self.op2.on_mouse_down(pos)
        self.op3.on_mouse_down(pos)
        self.op4.on_mouse_down(pos)

    def on_mouse_up(self, pos):
        self.op1.on_mouse_up(pos)
        self.op2.on_mouse_up(pos)
        self.op3.on_mouse_up(pos)
        self.op4.on_mouse_up(pos)
        

# below is the test code
with open('quiz_questions.json', 'r') as f:
    # load the data from the file
    quiz_data = json.load(f)

WIDTH = 800
HEIGHT = 600

backdrops = Actor("bg1")
backdrops.scale = 0.5
backdrops.pos=(400,300)

current_question=0
questions=[]

quiz_end = Option("question", "", pos=(400, 200))
quiz_end.show = False
quiz_end.scale=0.6

def question_answered():
    global current_question
    if(current_question<len(questions)-1):
       current_question+=1
       questions[current_question].start_entry()
    else:
        quiz_result = 0
        for q in questions:
            if q.current_answer == str(q.question["correct_answer"]):
                print("True")
                quiz_result +=1
            else:
                print("False")
        quiz_end.optiontext= "Congratulations! You have passed the test." if quiz_result>len(questions)/2 else "Sorry! You didn't passed the test, please try again"
        quiz_end.show = True

for question in quiz_data["questions"]:
    q = Question(question, callback=question_answered)
    questions.append(q)

questions[current_question].start_entry()

def draw():
    screen.clear()
    backdrops.draw()
    questions[current_question].draw()
    quiz_end.draw()

def on_mouse_down(pos):
    questions[current_question].on_mouse_down(pos)

def on_mouse_up(pos):
    questions[current_question].on_mouse_up(pos)

pgzrun.go()
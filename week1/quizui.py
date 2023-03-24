import pygame
import pgzrun
from pgzhelper import *

mod = sys.modules['__main__']

class Option(Actor):
    def __init__(self, btnname, pos,  message, order="", callback=None, show=True):
        super().__init__(btnname + '_up', pos)
        self.btnname = btnname
        self.callback = callback
        self.order = order
        self.message = message
        self.show = show
        self.selected = False

    def on_mouse_down(self, pos):
        if self.show and self.collidepoint(pos):
            self.image = self.btnname + '_down'

    def on_mouse_up(self, pos):
        if self.show and self.collidepoint(pos):
            # self.image = self.btnname + '_up'
            self.selected = True
            if self.callback:
                self.callback(self.message)

    def draw(self):
        if self.show:
            topleft=self.topleft
            x=topleft[0]
            y=topleft[1]
            mod.screen.draw.textbox(str(self.order)+self.message, (x+self.width/11, y+self.height/8, self.width-self.width/11*2, self.height-self.height/8*2) )
            super().draw()

# question1 = {
#     "description" : "What's the answer of 1+3?",
#     "options" : [1, 2, 3, 4],
#     "correct_answer" : 4,
#     "response" : ["You are correct", "It's wrong, you need do something else."]
# }

class Question():
    def __init__(self, question=None, select_callback=None):
        self.ops=[]
        self.question = question
        self.q = Option("question", pos=(400, 100), message="")
        self.select_callback = select_callback

    def option_clicked(self):
        for op in self.ops:
            if self.question and op.selected and op.message == self.question["correct_answer"]:
                self.question.iscorrect = True
        

    def display_options(self, question):
        self.ops.clear()
        self.question = question
        options = question["options"]
        self.ops.append(Option("option", pos=(200, 400), order="A. ", message=str(options[0]), callback=self.select_callback))
        self.ops.append(Option("option", pos=(600, 400), order="B. ", message=str(options[1]), callback=self.select_callback))
        self.ops.append(Option("option", pos=(200, 480), order="C. ", message=str(options[2]), callback=self.select_callback))
        self.ops.append(Option("option", pos=(600, 480), order="D. ", message=str(options[3]), callback=self.select_callback))

        self.q = Option("question", pos=(400, 150), message=question["description"])
        self.q.scale = 0.5

    def draw(self):
        self.q.draw()
        for opt in self.ops:
            opt.draw()

    def on_mouse_down(self, pos):
        for opt in self.ops:
            opt.on_mouse_down(pos)
    
    def on_mouse_up(self, pos):
        for opt in self.ops:
            opt.on_mouse_up(pos)

import pygame
import pgzrun
from pgzhelper import *

mod = sys.modules['__main__']

class Option(Actor):
    def __init__(self, btnname, pos, message, callback=None, show=True):
        super().__init__(btnname + '_up', pos)
        self.btnname = btnname
        self.callback = callback
        self.message = message
        self.show = show

    def on_mouse_down(self, pos):
        if self.show and self.collidepoint(pos):
            self.image = self.btnname + '_down'

    def on_mouse_up(self, pos):
        if self.show and self.collidepoint(pos):
            self.image = self.btnname + '_up'
            if self.callback:
                self.callback()

    def draw(self):
        if self.show:
            mod.screen.draw.textbox(self.message, (self.topleft[0]+25, self.topleft[1]+5, self.width-60, self.height-10) )
            super().draw()

# question1 = {
#     "description" : "What's the answer of 1+3?",
#     "options" : [1, 2, 3, 4],
#     "correct_answer" : 4
# }

class Question():
    def __init__(self,):
        self.ops=[]

    def display_options(self, question):
        self.ops.clear()
        options = question["options"]
        self.ops.append(Option("option", pos=(200, 400), message="A. " + str(options[0])))
        self.ops.append(Option("option", pos=(600, 400), message="B. " + str(options[1])))
        self.ops.append(Option("option", pos=(200, 480), message="C. " + str(options[2])))
        self.ops.append(Option("option", pos=(600, 480), message="D. " + str(options[3])))

        q = Option("option", pos=(400, 100), message=question["description"])
        q.scale = 2.5
        

    
    def draw(self):
        for opt in self.ops:
            opt.draw()

    def on_mouse_down(self, pos):
        for opt in self.ops:
            opt.on_mouse_down(pos)
    
    def on_mouse_up(self, pos):
        for opt in self.ops:
            opt.on_mouse_up(pos)

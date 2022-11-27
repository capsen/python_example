
import pyzgame1
# import pgzrun

from pgzero.builtins import Actor, animate, keyboard, screen

WIDTH = 300
HEIGHT = 300

actor1 = Actor('p3_stand')
actor1.pos = 100, 56

actor1.topright = 0, 10


def draw():
    # set screen background color
    screen.fill((128,0,0))
    actor1.draw()

def update():
    actor1.left += 2
    if actor1.left > WIDTH:
        actor1.right = 0

# pgzrun.go()
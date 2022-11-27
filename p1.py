import pgzrun

WIDTH = 800
HEIGHT = 600

p3 = Actor("p3_stand")
p3.pos = (400, 400)
p3.images= ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
p3.imageindex=0

timestamp = 0

def draw():
    global timestamp
    # screen.fill((128, 0, 0))
    screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    screen.draw.text(str(timestamp), (50, 30), color="orange")
    p3.draw()

def update():
    # p3.left += 2

    global timestamp
    timestamp+=1
    if(timestamp%1==0):
        p3.imageindex = 0 if p3.imageindex>=len(p3.images)-1 else p3.imageindex+1
        p3.image=p3.images[p3.imageindex]
        # timestamp=0
    
    if p3.left > WIDTH:
        p3.right = 0

pgzrun.go() # Must be last line
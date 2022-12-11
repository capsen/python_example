import pgzrun

WIDTH = 800
HEIGHT = 600

p3 = Actor("p3_stand")
p3.pos = (100, 400)
p3.images= ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
p3.imageindex = 0

p3.velocity_y = 0
p3.gravity = 1

obstacles = []
obstacles_timeout = 0
score=0
game_over = False


def draw():
    # screen.fill((0,255,0))
    screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    #screen.draw.text("hello world", (100, 100), fontname="bauhs93", fontsize=32)
    if game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)
        screen.draw.text('Score: ' + str(score), centerx=400, centery=330, color=(255,255,255), fontsize=60)
    else:
        screen.draw.text('Score: ' + str(score), (15,10), fontname="bauhs93", color=(0,0,0), fontsize=30)
        p3.draw()

        for actor in obstacles:
            actor.draw()
    
    

def update():
    # move object
    # p3.left += 2
    # if(p3.left>800):
    #     p3.right = 0
    global obstacles, obstacles_timeout, score, game_over

    
    # change image
    if(p3.imageindex > len(p3.images)-1):
        p3.imageindex=0
    p3.image=p3.images[p3.imageindex]
    p3.imageindex += 1

    # jump when space pressed
    if keyboard.space:
        # set initial velocity
        p3.velocity_y = -10
        if p3.y==400:
            sounds.jump.play()
        
        if game_over:
            score=0
            p3.velocity_y = 0
            game_over=False
    # move base on velocity
    p3.y += p3.velocity_y

    # update the velocity base on gravity
    p3.velocity_y += p3.gravity

    # if hit the ground correct the velocity and position
    if p3.y > 400:
        p3.velocity_y = 0
        p3.y = 400
    
    # detect hit obstacle
    if p3.collidelist(obstacles) != -1:
        game_over = True
    
    # set obstacles
    obstacles_timeout += 1
    if obstacles_timeout > 50 and not game_over:
        actor = Actor('cactus')
        actor.x = 850
        actor.y = 400
        obstacles.append(actor)
        obstacles_timeout = 0

    for actor in obstacles:
        actor.x -= 8
        if actor.right < 0: 
            obstacles.remove(actor)
            if not game_over: 
                score += 1
        


pgzrun.go() # Must be last line
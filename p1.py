import pgzrun

WIDTH = 800
HEIGHT = 600

obstacles=[]
obstacles_timeout=0
score=0
game_over= False

p3 = Actor("p3_stand")
p3.pos = (100, 400)
p3.images= ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
p3.imageindex = 0
p3.velocity_y = 0
p3.gravity = 2
p3.jumping = False

def draw():
    # screen.fill((0,255,0))
    screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

    if game_over:
        screen.draw.text("Game over", centerx=400, centery=270, color=(0, 0, 0), fontname="bauhs93", fontsize=32)
        screen.draw.text("score: "+str(score), centerx=400, centery=330, color=(0, 0, 0), fontname="bauhs93", fontsize=32)
    else:
        screen.draw.text("score: "+str(score), (20,100), color=(0, 0, 0), fontname="bauhs93", fontsize=32)
        p3.draw()
        for obstacle in obstacles:
            obstacle.draw()

def update():
    # move p3
    # p3.left += 2
    # if(p3.left>800):
    #     p3.right = 0
    global obstacles_timeout, score, game_over

    if(p3.imageindex > len(p3.images)-1):
        p3.imageindex=0
    p3.image=p3.images[p3.imageindex]
    p3.imageindex += 1

    # make p3 jump if space pressed
    if keyboard.space or keyboard.up:
        p3.velocity_y = -15
        if not p3.jumping:
            sounds.jump.play()
            p3.jumping=True
        if game_over:
            game_over = False
            score=0
            p3.velocity_y=0
            p3.y=400

        
    p3.y += p3.velocity_y

    p3.velocity_y+=p3.gravity

    if p3.y>400:
        p3.velocity=0
        p3.y=400
        p3.jumping=False

    
    obstacles_timeout +=1
    if obstacles_timeout > 50 and not game_over:
        obstacle = Actor('cactus')
        obstacle.x = 850
        obstacle.y = 400
        obstacles.append(obstacle)
        obstacles_timeout = 0

    for obstacle in obstacles:
        obstacle.left -= 8
        if obstacle.right < 0:
            obstacles.remove(obstacle)
            if not game_over:
                score += 1
    
    if p3.collidelist(obstacles) != -1:
        game_over=True


pgzrun.go() # Must be last line
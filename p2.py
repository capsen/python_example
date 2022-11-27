import pgzrun

WIDTH=800
HEIGHT=600

runner = Actor('p3_walk01')
run_images = ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
runner.images = run_images
runner.x = 100
runner.y = 400

velocity_y = 0
gravity = 1

def update():
  global velocity_y
  runner.next_image()

  if keyboard.up:
    velocity_y = -15

  runner.y += velocity_y
  velocity_y += gravity
  if runner.y > 400:
    velocity_y = 0
    runner.y = 400

def draw():
  screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
  screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
  runner.draw()

pgzrun.go() # Must be last line
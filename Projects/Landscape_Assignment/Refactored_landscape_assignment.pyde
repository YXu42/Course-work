x_animated = 0
y_animated = 1
x_increments = 0.1

def setup():
    size(640, 580)

def draw():
    #x_animated, x_increments, and y_increments are used to change location
    global x_animated, y_animated, x_increments
    
    movement_changes()
    
    background(114, 170, 255)
    noStroke()
    
    draw_sun()
    draw_land(0, 420)
    draw_clouds(139, 230)
    draw_bushes(78, 451)
    draw_overlay()

def movement_changes():
    global x_animated, y_animated, x_increments
    x_animated += x_increments
    
    #controls sun and yellow overlay
    if y_animated >= -200:
        y_animated -= 0.07
        
    #controls movement of clouds
    if x_animated >= 400:
        x_increments = -0.1
    elif x_animated <= 0:
        x_increments = 0.1

def draw_sun():
    fill(255, 170, 0)
    #sun
    ellipse(width/2, 410 + y_animated, 150, 150)
    
def draw_land(x, y):
    fill(49, 126, 24)
    #land
    rect(x, y, 640, 580)
    ellipse(x + 120, y + 30, 300, 100)
    ellipse(x + 292, y + 20, 150, 50)
    ellipse(x + 480, y + 20, 300, 100)
    ellipse(x + 640, y + 30, 300, 100)
    
def draw_clouds(x, y):
    fill(255, 255, 255, 220)
    #big cloud
    ellipse(x_animated + x, y, 100, 50)
    ellipse(x_animated + x + 30, y + 30, 96, 60)
    ellipse(x_animated + x - 30, y + 30, 96, 60)
    ellipse(x_animated + x - 50, y - 10, 96, 60)
    
    #smaller cloud
    ellipse((x_animated * -1) + x + 361, y - 110, 100, 50)
    ellipse((x_animated * -1) + x + 311, y - 140, 96, 60)
    
    #smallest cloud
    ellipse((x_animated * -1) + x + 361, y + 120, 100, 50)
    
def draw_bushes(x, y):
    fill(38, 93, 8)
    # bush #1 (far left)
    ellipse(x, y, 30, 30)
    ellipse(x + 22, y - 19, 50, 50)
    ellipse(x + 43, y - 13, 40, 40)
    ellipse(x + 62, y - 15, 40, 40)
    ellipse(x + 69, y - 3, 30, 30)
    ellipse(x + 21, y + 8, 30, 10)
    ellipse(x + 7, y + 12, 30, 10)
    ellipse(x + 39, y + 9, 40, 20)
    ellipse(x + 62, y + 8, 30, 10)
    
    #bush #2 (top right)
    ellipse(x + 474, y - 61, 50, 40)
    ellipse(x + 498, y - 75, 50, 40)
    ellipse(x + 520, y - 67, 50, 40)
    ellipse(x + 499, y - 61, 50, 40)
    ellipse(x + 523, y - 57, 40, 30)
    
    #bush #3 (middle)
    ellipse(x + 372, y + 33, 50, 40)
    ellipse(x + 386, y + 54, 50, 40)
    ellipse(x + 354, y + 55, 50, 40)
    ellipse(x + 322, y + 55, 50, 40)
    ellipse(x + 338, y + 39, 50, 40)
    
def draw_overlay():
    fill(255, 225, 0 + ((y_animated + 15) * -3.25), 90)
    #overlay
    rect(0, 0, width, height)

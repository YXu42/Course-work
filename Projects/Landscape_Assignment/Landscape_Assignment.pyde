x = 0
y = -30

def setup():
    size(640, 580)

def draw():
    global x, y
    x += 0.1
    background(114, 170, 255)
    noStroke()
    
    fill(255, 170, 0)
    ellipse(width/2, 440 + y, 150, 150)
    
    fill(20, 124, 33)
    rect(0, 450 + y, 640, 580)
    
    fill(255, 255, 0, 100)
    rect(0, 0, 640, 580)
    
    fill(255, 255, 255)
    ellipse(x + 139, height/2 - 30 + y, 100, 50)
    ellipse(x + 169, height/2 + y, 96, 60)
    ellipse(x + 109, height/2 + y, 96, 60)
    ellipse(x + 89, height/2 - 40 + y, 96, 60)
    
    ellipse((x * -1) + 500, 150 + y, 100, 50)
    ellipse((x * -1) + 450, 120 + y, 96, 60)
    
    ellipse((x * -1) + 500, 380 + y, 100, 50)

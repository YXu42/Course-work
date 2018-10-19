x = 0

def setup():
    size(640, 580)

def draw():
    global x
    background(114, 170, 255)
    noStroke()
    fill(255, 170, 0)
    ellipse(width/2, 440, 150, 150)
    fill(7, 156, 2)
    rect(0, 440, 640, 580)
    fill(255, 255, 0, 100)
    rect(0, 0, 640, 580)
    fill(255, 255, 255)
    ellipse(x + 139, height/2, 100, 50)
    ellipse(x + 169, height/2 + 30, 96, 60)
    ellipse(x + 109, height/2 + 30, 96, 60)
    ellipse(x + 89, height/2 - 10, 96, 60)
    
    ellipse(x + 500, 150, 100, 50)
    ellipse(x + 450, 120, 96, 60)
    
    

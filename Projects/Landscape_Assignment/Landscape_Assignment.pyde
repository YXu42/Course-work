xA = 0
y = -30
yA = 1
xincrements = 0.1

def setup():
    size(640, 580)

def draw():
    global xA, y, yA, xincrements
    
    xA += xincrements
    
    if yA >= -200:
        yA -= 0.07
        
    if xA >= 400:
        xincrements = -0.1
    elif xA <= 0:
        xincrements = 0.1
    
    background(114, 170, 255)
    noStroke()
    
    fill(255, 170, 0)
    ellipse(width/2, 410 + yA, 150, 150)  #sun
    
    fill(49, 126, 24)
    rect(0, 450 + y, 640, 580) #land
    ellipse(120, 470 + y, 300, 100)  #hills
    ellipse(292, 460 + y, 150, 50)
    ellipse(480, 460 + y, 300, 100)
    ellipse(640, 470 + y, 300, 100)
    
    fill(255, 225, 0 + ((yA + 15) * -3.25), 90)
    rect(0, 0, 640, 580)  #yellow overlay
    
    fill(255, 255, 255, 220)
    ellipse(xA + 139, height/2 - 30 + y, 100, 50)  #big cloud
    ellipse(xA + 169, height/2 + y, 96, 60)
    ellipse(xA + 109, height/2 + y, 96, 60)
    ellipse(xA + 89, height/2 - 40 + y, 96, 60)
    
    ellipse((xA * -1) + 500, 150 + y, 100, 50)  #smaller cloud
    ellipse((xA * -1) + 450, 120 + y, 96, 60)
    
    ellipse((xA * -1) + 500, 380 + y, 100, 50)  #smallest cloud
    
    #fill(25, 100, 0)
    fill(45, 118, 22)
    ellipse(78, 451, 30, 30)  # bush #1
    ellipse(100, 432, 50, 50)
    ellipse(121, 438, 40, 40)
    ellipse(140, 436, 40, 40)
    ellipse(147, 448, 30, 30)
    ellipse(121, 447, 30, 30)
    ellipse(99, 459, 30, 10)
    ellipse(85, 463, 30, 10)
    ellipse(117, 460, 40, 20)
    ellipse(140, 459, 30, 10)
    
    ellipse(552, 390, 50, 40)  #bush #2
    ellipse(576, 376, 50, 40)
    ellipse(598, 384, 50, 40)
    ellipse(577, 390, 50, 40)
    ellipse(601, 394, 40, 30)
    
    ellipse(450, 484, 50, 40)  #bush #3
    ellipse(464, 505, 50, 40)
    ellipse(432, 506, 50, 40)
    ellipse(400, 506, 50, 40)
    ellipse(416, 490, 50, 40)
    
    fill(255, 255, 255)
    textSize(10)
    text(str(mouseX) + ", " + str(mouseY), mouseX, mouseY)

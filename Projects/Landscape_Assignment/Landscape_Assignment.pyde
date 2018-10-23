x_animated = 0
y = 0
y_animated = 1
x_increments = 0.1

def setup():
    size(640, 580)

def draw():
    global x_animated, y, y_animated, x_increments  #x_animated and y_animated is used to change x and y locations,
                                                    #y is there in case landscape needs to be shifted, didn't want to tie to height
                                                    #x-increments are used to control the speed of objects horizontally 
    
    x_animated += x_increments  #used to change x value for some objects
    
    if y_animated >= -200:  #controls sun and yellow overlay
        y_animated -= 0.07
        
    if x_animated >= 400:  #controls movement of clouds
        x_increments = -0.1
    elif x_animated <= 0:  #changes direction by changing x_increments
        x_increments = 0.1
    
    background(114, 170, 255)
    noStroke()
    
    fill(255, 170, 0)
    ellipse(width/2, 410 + y_animated, 150, 150)  #sun
    
    fill(49, 126, 24)
    rect(0, 420 + y, 640, 580)  #land
    ellipse(120, 450 + y, 300, 100)  #hills
    ellipse(292, 440 + y, 150, 50)
    ellipse(480, 440 + y, 300, 100)
    ellipse(640, 450 + y, 300, 100)
    
    fill(255, 255, 255, 220)
    ellipse(x_animated + 139, 230 + y, 100, 50)  #big cloud
    ellipse(x_animated + 169, 260 + y, 96, 60)
    ellipse(x_animated + 109, 260 + y, 96, 60)
    ellipse(x_animated + 89, 220 + y, 96, 60)
    
    ellipse((x_animated * -1) + 500, 120 + y, 100, 50)  #smaller cloud
    ellipse((x_animated * -1) + 450, 90 + y, 96, 60)
    
    ellipse((x_animated * -1) + 500, 350 + y, 100, 50)  #smallest cloud
    
    fill(38, 93, 8)
    ellipse(78, 451, 30, 30)  # bush #1 (far left)
    ellipse(100, 432, 50, 50)
    ellipse(121, 438, 40, 40)
    ellipse(140, 436, 40, 40)
    ellipse(147, 448, 30, 30)
    ellipse(99, 459, 30, 10)
    ellipse(85, 463, 30, 10)
    ellipse(117, 460, 40, 20)
    ellipse(140, 459, 30, 10)
    
    ellipse(552, 390, 50, 40)  #bush #2 (top right)
    ellipse(576, 376, 50, 40)
    ellipse(598, 384, 50, 40)
    ellipse(577, 390, 50, 40)
    ellipse(601, 394, 40, 30)
    
    ellipse(450, 484, 50, 40)  #bush #3 (middle)
    ellipse(464, 505, 50, 40)
    ellipse(432, 506, 50, 40)
    ellipse(400, 506, 50, 40)
    ellipse(416, 490, 50, 40)
    
    fill(255, 225, 0 + ((y_animated + 15) * -3.25), 90)
    rect(0, 0, 640, 580)  #yellow overlay (changes colour until sun stops)

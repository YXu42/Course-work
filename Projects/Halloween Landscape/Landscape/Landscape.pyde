import random

x = 0
timer = 0
random_x = 50
random_y = 50

def setup():
    global gallo_pic
    size(640, 580)
    #gallo_pic = loadImage("https://www.clipartmax.com/png/middle/8-86302_free-to-use-public-domain-zombie-clip-art-zombie-clipart-transparent-background.png")
    #imageMode(CENTER)
    
def draw():
    global x, timer, random_x, random_y
    timer += 1
    
    #if timer == random.randint(timer, 450):
       # x = 240
       # timer = 0
    
    if x >= 0:
        x -= 1.5
    background(87, 82, 100)
    noStroke()
    
    fill(255, 255, 255)
    triangle(random_x, random_y, random_x - 40, random_y + 70, random_x - 20, random_y + 90)
    
    cloud(537, 75)
    cloud(13, 83)
    cloud(370, 93)
    cloud(180, 72)
    
    #Land at back
    fill(58, 72, 63)
    ellipse(523, 431, 500, 200)
    
    #Land at middle
    fill(72, 90, 78)
    ellipse(120, 458, 550, 200)
    
    #Land in front
    fill(81, 100, 87)
    ellipse(140, 571, 600, 300)
    ellipse(509, 488, 700, 200)
    
    #Test zombie
    #gallo_pic.resize(150, 0)
    #image(gallo_pic, 435, 459)
    
    rectMode(CORNERS)
    fill(255, x)
    rect(0, 0, width, height)
    
    fill(255, 255, 255)
    textSize(10)
    text(str(mouseX) + ", " + str(mouseY), mouseX, mouseY)
    
def cloud(x_location, y_location):
    #159, 80
    fill(100, 99, 99, 220)
    ellipse(x_location, y_location, 100, 70)
    ellipse(x_location + 65, y_location - 18, 103, 73)
    ellipse(x_location + 126, y_location - 3, 100, 70)
    ellipse(x_location + 40, y_location + 34, 100, 50)
    ellipse(x_location + 120, y_location + 30, 97, 57)

"""
This program starts off by drawing three stars (make sure it works).
Do the following in steps:
1. Increase the number of stars to 5.
2. Rather than calling an ellipse function for each star, 
   create a while loop with an index variable to draw them.
3. Rather than manually adding stars, create a for loop that will add 100
   stars to the stars_x and stars_y lists with random x/y coordinates.
4. Create a for loop to increase the x location ever so slightly to make the 
   stars move across the sky.
5. Within the draw loop, use the list.append() method on both lists to 
   periodically add another star. Add the star off-screen and let it move into view.
   - You need to limit the number of times per second a new star is added, or there
     will be too many created (60 per second). Use frameCount % 60 == 0 to create one every 60 frames.
6. If any particular star has moved out of view, remove it from the lists. Use list.pop(index) to remove
   the appropriate coordinates.
7. Convert the two coordinate lists into a 2-dimensional list called 'stars'. The general structure will be:
   stars = [[x1, y2], [x2, y2], [x3, y3]]
   stars[0]     # the first star as a list of coordinates [x1, y1]
   stars[0][0]  # the first star's x coordinate, x1
   stars[0][1]  # the first star's y coordinate, y1
"""

# two lists with three stars' xy coordinates
# (50, 200), (100, 250), (150, 300)

import random

stars = []

for star in range(0, 100):
    stars.append([random.randint(0, 640), random.randint(0, 480)])

def setup():
    size(640, 480)

def draw():
    drawn_stars = 0
            
    background(0)
    
    noStroke()
    fill(255)
   
    if frameCount % 60 == 0:
        stars.append([random.randint(-640, 0), random.randint(0, 480)])
   
    for star in range(0, len(stars)):
       stars[star][0] += 0.1
        
    for star in range(len(stars) - 1, 0, -1):   #For loop removes stars from back of list to front to avoid index error
        if stars[star][0] >= width:
            stars.pop(star)
    
    #Another version with a for loop instead of a while loop
    #for star in range(0, len(stars)):
    #    ellipse(stars[star][0], stars[star][1], 5, 5)
    
    while drawn_stars <= len(stars) - 1:
        ellipse(stars[drawn_stars][0], stars[drawn_stars][1], 5, 5)
        drawn_stars += 1

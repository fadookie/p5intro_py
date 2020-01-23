# Start working with colors

ALWAYS_PAINT = True

def setup():
    size(800, 800)
    noStroke()
    '''
    We change the color mode to HSB (Hue, Saturation, Brightness) to make it easier to work with.
    I use http://colorizer.org/ to show the differences.
    RGB is closer to what computer needs to control screen pixels (primary colors of light) but unweidly.
    Try mixing a specific color using RGB sliders - hard to do by hand or programatically.
    HSB/HSV provides a more convenient representation to quickly zero in on the desired color.
    
    Second parameter is range. I find normalized values (0 - 1) more convenient to work with as it maps
    directly to the percentile value you get when dividing any number by its maximum range.
    '''
    colorMode(HSB, 1)

def draw():
    background(0.5) # 50% middle gray is now represented by 0.5 insted of 128
    if (ALWAYS_PAINT or mousePressed):
        fill(0.5, 1, 1); # Sets fill color of ellipse to cyan, the hue halfway between red and violet (can show on colorizer)
        ellipse(mouseX, mouseY, 100, 100)

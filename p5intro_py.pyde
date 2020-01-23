# Only paint while mouse depressed
def setup():
    size(800, 800)
    noStroke()

def draw():
    # background(128)
    if (mousePressed):
        ellipse(mouseX, mouseY, 100, 100)

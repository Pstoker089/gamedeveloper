import pgzrun
from random import randint


TITLE="Alien shooter"

WIDTH=500
HEIGHT=500

alien=Actor("alien")
alien.pos=250,250
message=""


def draw():
    screen.fill("blue")
    screen.draw.text(message,(370,10),fontsize=30)
    alien.draw()

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        #alien.pos=randint(50,450),randint(50,450)
        message="Good shot"
        sounds.eep.play()
    else:
        message="You missed"

def update():
    alien.x+=9
    if alien.left>=500:
        alien.right=0
        alien.y=randint(50,450)

pgzrun.go()
    
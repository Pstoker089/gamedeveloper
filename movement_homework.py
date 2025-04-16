import pgzrun
from random import randint

TITLE="Guy catcher"

WIDTH=500
HEIGHT=500

guy=Actor("little_fellow")
guy.pos=250,250
message=""

def draw():
    screen.fill("black")
    screen.draw.text(message,(370,10),fontsize=30)
    guy.draw()

def on_mouse_down(pos):
    global message
    if guy.collidepoint(pos):
        message="You got him!"
        sounds.eep.play()
    else:
        message="You missed!"

def update():
    guy.y+=8
    guy.x+=8
    if guy.left>=500 or guy.bottom>=500:
        guy.right=randint(0,250)
        guy.y=randint(0,250)

pgzrun.go()
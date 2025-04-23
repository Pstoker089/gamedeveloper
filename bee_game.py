import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

bee=Actor("bee")
bee.pos=250,250
flower=Actor("flower")
flower.pos=randint(75,525),randint(75,525)
score=0

gameover=False

def draw():
    screen.blit("field",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+ str(score) ,(370,10),fontsize=30)

    if gameover:
        screen.fill("yellow")
        screen.draw.text("You scored "+str(score), (300,250),fontsize=40, color="black")

def update():
    global score
    if keyboard.left:
        bee.x-=5
    if keyboard.right:
        bee.x+=5
    if keyboard.up:
        bee.y-=5
    if keyboard.down:
        bee.y+=5
    if bee.colliderect(flower):
        flower.pos=randint(50,550),randint(50,550)
        score+=10
def timer():
    global gameover
    gameover=True

clock.schedule(timer,10)

pgzrun.go()
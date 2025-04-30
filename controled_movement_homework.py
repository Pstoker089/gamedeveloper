import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

fellow=Actor("little_fellow")
fellow.pos=250,250
food=Actor("spaghetti")
food.pos=randint(75,525),randint(75,525)
score=0


gameover=False

def draw():
    screen.fill("black")
    fellow.draw()
    food.draw()
    screen.draw.text("Score: "+ str(score) ,(370,10),fontsize=30)

    if gameover:
        screen.fill("purple")
        screen.draw.text("You scored "+ str(score), (300,250),fontsize=40)

def update():
    global score
    if keyboard.left:
        fellow.x-=10
    if keyboard.right:
        fellow.x+=10
    if keyboard.up:
        fellow.y-=10
    if keyboard.down:
        fellow.y+=10
        if fellow.colliderect(food):
            food.pos=randint(50,550),randint(50,550)
            score+=1


  
def timer():
    global gameover
    gameover=True

clock.schedule(timer,10)

pgzrun.go()
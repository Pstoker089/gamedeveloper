import pgzrun
from random import randint
gifts=[]

WIDTH=600
HEIGHT=500
score=0
gameover=False
exit=False
test=Actor("little_fellow")
test.pos=250,250
for i in range(2):
    heart=Actor("heart")
    heart.pos=randint(50,450),randint(50,450)
    flower=Actor("flower")
    flower.pos=randint(50,450),randint(50,450)
    gifts.append(heart)
    gifts.append(flower)

def draw():
    screen.blit("field",(0,0))
    test.draw()
    for i in gifts:
        i.draw()
    if gameover:
        screen.blit("mothers_day3",(0,0))

def finish():
    global gameover
    gameover==True

def update():
    global score
    global gameover
    global exit
    if exit:
        gameover=True
    if keyboard.left:
        test.x-=5
    if keyboard.right:
        test.x+=5
    if keyboard.up:
        test.y-=5
    if keyboard.down:
        test.y+=5
    for i in gifts:
        if test.colliderect(i):
            i.pos=randint(50,450),randint(50,450)
            score+=1
            if score==50:
                exit=True
        
        


pgzrun.go()
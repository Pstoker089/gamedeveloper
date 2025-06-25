import pgzrun

WIDTH=1000
HEIGHT=600

gameover=False
movedown=False
dirrection=1
enemies=[]
bullets=[]
score=0

ship=Actor("galaga_ship")
ship.pos=300,515

for i in range(6):
    for j in range(4):
        enemy=Actor("galaga_enemy")
        enemies.append(enemy)
        enemies[-1].x=100+(50*i)
        enemies[-1].y=100+(50*j)

def draw():
    screen.fill("blue")
    for i in enemies:
        i.draw()
    ship.draw()
    for j in bullets:
        j.draw()
    
    if gameover==True:
        screen.draw.text("GAME OVER",(500,300), fontsize=40, color="black")
    

def update():
    global movedown
    global dirrection
    global score
    global gameover
    movedown=False
    if keyboard.left:
        ship.x-=5
    if keyboard.right:
        ship.x+=5
        
    for i in bullets:
        if i.y<=0:
            bullets.remove(i)
        else:
            i.y-=5
    
    if len(enemies)>0 and (enemies[0].x<0 or enemies[-1].x>950):
        movedown=True
        dirrection*=-1
    
    for i in enemies:
        i.x+=3*dirrection
        if movedown==True:
            i.y+=10
        if i.y>=600:
            enemies.remove(i)
        #enemy movement
        for j in bullets:
            if i.colliderect(j):
                enemies.remove(i)
                bullets.remove(j)
                score+=100
                if len(enemies)==0:
                    gameover=True
        #bullets colision



def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("galaga_bullet")
        bullets.append(bullet)
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-80


pgzrun.go()
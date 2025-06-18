import pgzrun

WIDTH=1000
HEIGHT=600

dirrection=1
enemies=[]
bullets=[]

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
    

def update():
    global dirrection
    if keyboard.left:
        ship.x-=5
    if keyboard.right:
        ship.x+=5
        
    for i in bullets:
        if i.y<=0:
            bullets.remove(i)
        else:
            i.y-=5
    
    for i in enemies:
        if dirrection==1:
            i.x+=1
            if i.x==550:
                dirrection=-1
        elif dirrection==-1:
            i.x-=1
            if i.x==50:
                dirrection=1
    

def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("galaga_bullet")
        bullets.append(bullet)
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-80









pgzrun.go()
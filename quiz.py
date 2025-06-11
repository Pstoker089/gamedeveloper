import pgzrun

TITLE="FUN QUIZ"
WIDTH=800
HEIGHT=800

questions=[]

currentq=0
maxq=0
score=0
scrollerbox=Rect(0,0,800,80)
questionbox=Rect(25,100,600,120)
timerbox=Rect(655,100,120,120)
answerbox1=Rect(50,275,220,130)
answerbox2=Rect(380,275,220,130)
answerbox3=Rect(50,580,220,130)
answerbox4=Rect(380,580,220,130)
skipbox=Rect(655,245,120,535)

time=10
anserboxes=[answerbox1,answerbox2,answerbox3,answerbox4]
finish=False

def draw():
    global maxq
    global currentq
    scrollertext=f"WELCOME TO THE QUIZ | QUESTION NUMBER {currentq} out of {maxq} | "
    screen.fill("black")
    screen.draw.filled_rect(scrollerbox,"dark green")
    screen.draw.filled_rect(questionbox,"orange")
    screen.draw.filled_rect(timerbox,"orange")
    screen.draw.filled_rect(answerbox1,"blue")
    screen.draw.filled_rect(answerbox2,"blue")
    screen.draw.filled_rect(answerbox3,"blue")
    screen.draw.filled_rect(answerbox4,"blue")
    screen.draw.filled_rect(skipbox,"yellow")
    screen.draw.textbox(scrollertext,scrollerbox,color="white")
    screen.draw.textbox("skip question",skipbox,color="white", angle=-90)
    screen.draw.textbox(str(time),timerbox,color="red")
    screen.draw.textbox(q[0],questionbox,color="white")
    j=1
    for i in anserboxes:
        screen.draw.textbox(q[j].strip(),i,color="white")
        j+=1
    
        
    

def qloader():
    global maxq
    with open("questions.txt") as file:
        for i in file:
            questions.append(i)
            maxq+=1

def read_qfile():
    global currentq
    global questions
    currentq+=1


    return questions.pop(0).split("|")

def on_mouse_down(pos):
    global anserboxes
    answercheck=1
    for i in anserboxes:
        if i.collidepoint(pos):
            if answercheck is int(q[5]):
                correctans()
            else:
                gameover()
        answercheck+=1
    if skipbox.collidepoint(pos):
        skipq()

def correctans():
    global time
    global score
    global q
    score+=1
    if questions:
        q=read_qfile()
        time=30
    else:
        gameover()
    

def gameover():
    global finish
    global q
    global time
    time=0
    gomessage=f"GAME OVER you got {score} out of {maxq} correct"
    q=[gomessage,"-","-","-","-","0"]
    finish=True

def skipq():
    global time
    global q
    if questions:
        q=read_qfile()
        time=30
    else:
        gameover()

def updtime():
    global time
    if time:
        time-=1
    else:
        gameover()

def update():
    scrollerbox.x-=5
    if scrollerbox.right<=0:
        scrollerbox.x=800
    


qloader()
q=read_qfile()
clock.schedule_interval(updtime,1)
pgzrun.go()
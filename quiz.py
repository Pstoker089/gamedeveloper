import pgzrun

TITLE="FUN QUIZ"
WIDTH=800
HEIGHT=800

questions=[]

currentq=0
maxq=0
scrollerbox=Rect(0,0,800,80)
questionbox=Rect(25,100,600,120)
timerbox=Rect(655,100,120,120)
answerbox1=Rect(50,275,220,130)
answerbox2=Rect(380,275,220,130)
answerbox3=Rect(50,580,220,130)
answerbox4=Rect(380,580,220,130)
skipbox=Rect(655,245,120,535)
scrollertext=f"WELCOME TO THE QUIZ | QUESTION NUMBER {currentq} out of {maxq} | "
time=30

def draw():
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

def qloader():
    global maxq
    with open("questions.txt") as file:
        for i in file:
            questions.append(i)
            maxq+=1




def update():
    scrollerbox.x-=5
    if scrollerbox.right<=0:
        scrollerbox.x=800
    


qloader()
print(questions)
pgzrun.go()
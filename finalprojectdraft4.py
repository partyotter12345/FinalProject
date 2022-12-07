from graphics import *
import random,sched,time

#define pointvalue
pointvalue = 0

#define window parameters
win = GraphWin('The Game', 1000,600)
win.yUp()


#Creation of Background
#Avery Update
def background():
    #define background
    lvl1 = Image(Point(500,300),"forestback.gif")
    lvl1.draw(win)
    
#Beginning Menu / Explanation
def begingame():

    startScreen = Rectangle(Point(0,0), Point(1000,600))
    startScreen.setFill('green')
    startScreen.draw(win)

    startMessage1 = Text(Point(500,450), 'A group of invaders are trying to steal your gold!')
    startMessage2 = Text(Point(500,375), 'To capture them you must click on them before they disappear')
    startMessage3 = Text(Point(500,300), 'To advance to the next level, you must capture at least 8 invaders')
    startMessage4 = Text(Point(500,100), 'Game will begin in 10 seconds...')

    startMessage1.setTextColor('black')
    startMessage2.setTextColor('black')
    startMessage3.setTextColor('black')
    startMessage4.setTextColor('black')

    startMessage1.setSize(22)
    startMessage2.setSize(22)
    startMessage3.setSize(22)
    startMessage4.setSize(22)

    startMessage1.setStyle('bold')
    startMessage2.setStyle('bold')
    startMessage3.setStyle('bold')
    startMessage4.setStyle('bold')

    startMessage1.draw(win)
    startMessage2.draw(win)
    startMessage3.draw(win)
    startMessage4.draw(win)

    time.sleep(2) #change this back to 10 after work
    
    startScreen.undraw()
    startMessage1.undraw()
    startMessage2.undraw()
    startMessage3.undraw()
    startMessage4.undraw()

    

    
def hitmarker(x,y,win):
    hitmarker = Text(Point(x,y), 'Hit!')
    hitmarker.setSize(16)
    hitmarker.setTextColor('green')
    hitmarker.draw(win)
    hitmarker.wait(0.5)
    hitmarker.undraw()
    
def pointcounterfunction(pointvalue,win):
    pointcounter = Text(Point(20, 20),pointvalue)
    pointcounter.setSize(18)
    pointcounter.setTextColor('white')
    pointcounter.draw(win)
    time.sleep(1)
    pointcounter.undraw()



def missmarker(x,y,win):
    missmarker = Text(Point(x,y), 'Miss :(')
    missmarker.setSize(16)
    missmarker.setTextColor('red')
    missmarker.draw(win)

#Purpose : To see if user has clicked on an enemy  
def nearenemy(x,y):

    global pointvalue

    clickpoint=win.checkMouse()
    
    if clickpoint != None:
        cx = x
        cy = y
        ux = clickpoint.getX()
        uy = clickpoint.getY()
    
        if abs(cx-ux)<=50 and abs(cy-uy)<=50:
            
            pointvalue +=1


            hitmarker(x,y,win)
            pointcounterfunction(pointvalue,win)
            
            
            
            
            
            
        else:
            pointcounter.undraw()
            pointvalue +=0
            pointcounter = Text(Point(20, 20),pointvalue)
            pointcounter.setSize(18)
            
            pointcounter.draw(win)
            
            time.sleep(1)
            

            
#enemy polygon          
def enemies(center,win,delay):
        
        #enemy head
        head = Circle(center, 30)
        head.setFill('red')
        head.draw(win)
                
        #left eye
        eye1Center = center.clone()
        eye1Center.move(-10,5)
        eye1 = Circle(eye1Center,6)
        eye1.setFill('green')
        eye1.draw(win)        

        #right eye
        eye2center = eye1Center.clone()
        eye2center.move(20,0)
        eye2 = Circle(eye2center,6)
        eye2.setFill('green')
        eye2.draw(win)       

        #left eyebrow
        eyeBrow1End1 = eye1Center.clone()
        eyeBrow1End1.move(-7,8)
        eyeBrow1End2 = eyeBrow1End1.clone()
        eyeBrow1End2.move(16,-4)
        eyeBrow1 = Line(eyeBrow1End1, eyeBrow1End2)
        eyeBrow1.setWidth(3)
        eyeBrow1.draw(win)
        
        #right eyebrow
        eyeBrow2End1 = eyeBrow1End2.clone()
        eyeBrow2End1.move(3,0)
        eyeBrow2End2 = eyeBrow2End1.clone()
        eyeBrow2End2.move(16,4)
        eyeBrow2 = Line(eyeBrow2End1, eyeBrow2End2)
        eyeBrow2.setWidth(3)
        eyeBrow2.draw(win)
        
        #mouth
        mouthCorner1 = center.clone()
        mouthCorner1.move(-10,-15)
        mouthCorner2 = mouthCorner1.clone()
        mouthCorner2.move(20,-5)
        mouth = Oval(mouthCorner1, mouthCorner2)
        mouth.setFill('black')
        mouth.draw(win)
        
        #nose
        nosePoint1 = center.clone()
        nosePoint1.move(0,-1)
        nosePoint2 = nosePoint1.clone()
        nosePoint2.move(-5, -5)
        nosePoint3 = nosePoint2.clone()
        nosePoint3.move(10,0)
        nosePoints = [nosePoint1, nosePoint2, nosePoint3]   
        nose = Polygon(nosePoints)
        nose.setFill('brown')
        nose.draw(win)
        
        time.sleep(delay)
        
        head.undraw()
        eye1.undraw()
        eye2.undraw()
        eyeBrow1.undraw()
        eyeBrow2.undraw()
        mouth.undraw()
        nose.undraw()

        
def levelone():
      
    for enemyspawn in list(range(10)):

        #find random x,y
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        enemies(center,win,1) #random center
        nearenemy(x,y) #nearenemy called

    if pointvalue >= 8:

        lvlonewinback = Rectangle(Point(0,0),Point(1000,600))
        lvlonewinback.setFill('grey')
        lvlonewinback.draw(win)

        winmessage = Text(Point(500,500), "Congratulations!")
        winmessage.setSize(36)
        winmessage.setStyle("bold")
        winmessage.setTextColor('yellow')

        winmessage2 = Text(Point(500,400), "You Pass Level One!")
        winmessage2.setSize(36)
        winmessage2.setStyle("bold")
        winmessage2.setTextColor('yellow')

        finalscore = "Your score was " +str(pointvalue)

        winmessage3 = Text(Point(500,300), finalscore)
        winmessage3.setSize(36)
        winmessage3.setStyle("bold")
        winmessage3.setTextColor('red')

        passmessage = Text(Point(500,200), "Wait 5 seconds for level Two!")
        passmessage.setSize(36)
        passmessage.setStyle("bold")
        passmessage.setTextColor('green')


        
        winmessage.draw(win)
        winmessage2.draw(win)
        winmessage3.draw(win)
        passmessage.draw(win)

        time.sleep(5)

        winmessage.undraw()
        winmessage2.undraw()
        winmessage3.undraw()
        passmessage.undraw()
        lvlonewinback.undraw()      

        levelTwo()
        
    else:
        lvl1LoseBack = Rectangle(Point (0,0), Point(1000,1000))
        lvl1LoseBack.setFill('black')
        lvl1LoseBack.draw(win)         
        
        GameOver = Text(Point(500,450), "GAME OVER")
        GameOver.setSize(36)
        GameOver.setStyle("bold")
        GameOver.setTextColor("red")
        GameOver.draw(win)

        LoseMessage = Text(Point(500,350), "YOU LOSE!")
        LoseMessage.setSize(36)
        LoseMessage.setStyle("bold")
        LoseMessage.setTextColor("red")
        LoseMessage.draw(win)
        win.promptClose(win.getWidth()/2, 20)
        


def levelTwo():
    global pointvalue
    pointvalue = 0

    for enemyspawn in list(range(10)):

        #find random x,y
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        time.sleep(random.randrange(1,3))
        enemies(center,win,0.75)
        nearenemy(x,y) #nearenemy called

    if pointvalue >= 8:

        lvltwowinback = Rectangle(Point(0,0),Point(1000,1000))
        lvltwowinback.setFill('grey')
        lvltwowinback.draw(win)

        win2message = Text(Point(500,500), "Congratulations!")
        win2message.setSize(36)
        win2message.setStyle("bold")
        win2message.setTextColor('yellow')

        win2message2 = Text(Point(500,400), "You Pass Level Two!")
        win2message2.setSize(36)
        win2message2.setStyle("bold")
        win2message2.setTextColor('yellow')

        final2score = "Your score was " +str(pointvalue)

        win2message3 = Text(Point(500,300), final2score)
        win2message3.setSize(36)
        win2message3.setStyle("bold")
        win2message3.setTextColor('red')

        passmessage2 = Text(Point(500,200), "Wait 5 seconds for level Two!")
        passmessage2.setSize(36)
        passmessage2.setStyle("bold")
        passmessage2.setTextColor('green')


        
        win2message.draw(win)
        win2message2.draw(win)
        win2message3.draw(win)
        passmessage2.draw(win)

        time.sleep(5)

        win2message.undraw()
        win2message2.undraw()
        win2message3.undraw()
        passmessage2.undraw()
        lvltwowinback.undraw()

        #levelthree() NOT MADE YET
        
    else:
        lvl2LoseBack = Rectangle(Point (0,0), Point(1000,1000))
        lvl2LoseBack.setFill('black')
        lvl2LoseBack.draw(win)         
        
        GameOver = Text(Point(500,450), "GAME OVER")
        GameOver.setSize(36)
        GameOver.setStyle("bold")
        GameOver.setTextColor("red")
        GameOver.draw(win)

        LoseMessage = Text(Point(500,350), "YOU LOSE!")
        LoseMessage.setSize(36)
        LoseMessage.setStyle("bold")
        LoseMessage.setTextColor("red")
        LoseMessage.draw(win)
        win.promptClose(win.getWidth()/2, 20)

def levelthree():
    pass

def main():

    begingame()
    background()
    levelone()

    
         
main()

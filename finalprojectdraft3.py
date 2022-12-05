from graphics import *
import random,sched,time

#define pointvalue
pointvalue = 0

#define window parameters
win = GraphWin('The Game', 1000,600)
win.yUp()




#Beginning Menu / Explanation
#NOT DONE
def begingame():
    pass

#Creation of Background
#Avery Update
def background():
    #define background
    lvl1 = Image(Point(500,300),"forestback.gif")
    lvl1.draw(win)
    

#Purpose : To see if user has clicked on an enemy  
def nearenemy(x,y,delay):

    global pointvalue

    clickpoint=win.checkMouse()
    

    if clickpoint != None:
        cx = x
        cy = y
        ux = clickpoint.getX()
        uy = clickpoint.getY()
    
        if abs(cx-ux)<=50 and abs(cy-uy)<=50:

            pointvalue +=1
            pointcounter = Text(Point(20, 20),pointvalue)            
            pointcounter.setSize(18)            
            pointcounter.draw(win)
            
            hitmarker = Circle(Point(x,y), 100)
            hitmarker.setWidth(4)
            hitmarker.setOutline('red')
            hitmarker.draw(win)
            time.sleep(delay)
            hitmarker.undraw()
            pointcounter.undraw()
            
        else:

            pointvalue +=0
            pointcounter = Text(Point(20, 20),pointvalue)
            pointcounter.setSize(18)
            pointcounter.draw(win)
            time.sleep(delay)
            pointcounter.undraw()

            
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
        
        

    
    


def game():

        
    for enemyspawn in list(range(10)):
        
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        enemies(center,win,1)
        nearenemy(x,y,1) #nearenemy called

    if pointvalue >= 8:
        lvlonewinback = Rectangle(Point(0,0),Point(1000,600))
        lvlonewinback.setFill('white')
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
        


def levelTwo():

    
    for enemyspawn in list(range(10)):
        
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        time.sleep(random.randrange(1,3))
        enemies(center,win,0.75)
        nearenemy(x,y,0.5) #nearenemy called

    if pointvalue >= 8:
        lvltwowinback = Rectangle(Point(0,0),Point(1000,1000))
        lvltwowinback.setFill('white')
        lvltwowinback.draw(win)

        win2message = Text(Point(500,500), "Congratulations!")
        win2message.setSize(36)
        win2message.setStyle("bold")
        win2message.setTextColor('yellow')

        win2message2 = Text(Point(500,400), "You Pass Level One!")
        win2message2.setSize(36)
        win2message2.setStyle("bold")
        win2message2.setTextColor('yellow')

        final2score = "Your score was " +str(pointvalue)

        win2message3 = Text(Point(500,300), finalscore)
        win2message3.setSize(36)
        win2message3.setStyle("bold")
        win2message3.setTextColor('red')


        
        win2message.draw(win)
        win2message2.draw(win)
        win2message3.draw(win)
        
    else:
        lvl2LoseBack = Rectangle(Point (0,0), Point(1000,1000))
        lvl2LoseBack.setFill('black')
        lvl2LoseBack.draw(win)         
        
        GameOver2 = Text(Point(500,450), "GAME OVER")
        GameOver2.setSize(36)
        GameOver2.setStyle("bold")
        GameOver2.setTextColor("red")
        GameOver2.draw(win)

        LoseMessage2 = Text(Point(500,350), "YOU LOSE!")
        LoseMessage2.setSize(36)
        LoseMessage2.setStyle("bold")
        LoseMessage2.setTextColor("red")
        LoseMessage2.draw(win)
        win.promptClose(win.getWidth()/2, 20)

        
def main():

    

    background()
    
    game()
    

    
        
    
    
    
main()


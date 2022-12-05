from graphics import *
import random,sched,time


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
            hitmarker = Circle(Point(x,y), 100)
            hitmarker.setWidth(4)
            hitmarker.setOutline('red')
            hitmarker.draw(win)
            time.sleep(0.2)
            hitmarker.undraw()


            pointcounter = Text(Point(20, 20),pointvalue)
            
            pointcounter.setSize(18)

            
            
            pointcounter.draw(win)

            time.sleep(1)

            pointcounter.undraw()
            
        else:

            pointvalue +=0
            pointcounter = Text(Point(20, 20),pointvalue)
            pointcounter.setSize(18)
            pointcounter.draw(win)
            time.sleep(1)
            pointcounter.undraw()

            
            
def enemies(x,y):

    #random enemy spawns, stays on screen for 1 secs

    pass
        




#def points():
   # pointvalue = pointvalue + 1
    


def gameFunction():

        
    for enemyspawn in list(range(10)):
        

        pointcounter = Text(Point(20, 20),pointvalue)
        pointcounter.setSize(18)
        pointcounter.undraw()
        pointcounter.draw(win)
        
        x=random.randint(50,950)
        y=random.randint(50,550)

        center = (Point(x,y))

        head = Circle(center, 30)
        head.setFill('red')
        head.draw(win)
    
        eye1Center = center.clone()
        eye1Center.move(-10,5)
        eye1 = Circle(eye1Center,6)
        eye1.setFill('green')
        eye1.draw(win)
    
        eye2center = eye1Center.clone()
        eye2center.move(20,0)
        eye2 = Circle(eye2center,6)
        eye2.setFill('green')
        eye2.draw(win)
        
        eyeBrow1End1 = eye1Center.clone()
        eyeBrow1End1.move(-7,8)
        eyeBrow1End2 = eyeBrow1End1.clone()
        eyeBrow1End2.move(16,-4)
        eyeBrow1 = Line(eyeBrow1End1, eyeBrow1End2)
        eyeBrow1.setWidth(3)
        eyeBrow1.draw(win)

        eyeBrow2End1 = eyeBrow1End2.clone()
        eyeBrow2End1.move(3,0)
        eyeBrow2End2 = eyeBrow2End1.clone()
        eyeBrow2End2.move(16,4)
        eyeBrow2 = Line(eyeBrow2End1, eyeBrow2End2)
        eyeBrow2.setWidth(3)
        eyeBrow2.draw(win)
    
        mouthCorner1 = center.clone()
        mouthCorner1.move(-10,-15)
        mouthCorner2 = mouthCorner1.clone()
        mouthCorner2.move(20,-5)
    
        mouth = Oval(mouthCorner1, mouthCorner2)
        mouth.setFill('black')
        mouth.draw(win)
    
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
                                   
        time.sleep(1)
        nearenemy(x,y) #nearenemy called
        head.undraw()
        eye1.undraw()
        eye2.undraw()
        eyeBrow1.undraw()
        eyeBrow2.undraw()
        mouth.undraw()
        nose.undraw()
        time.sleep(1)
        pointcounter.undraw()



def main():

    

    background()
    
    gameFunction()  

    win.promptClose(win.getWidth()/2, 20)
        
    
    
    
main()


from graphics import *
import random,sched,time

#define pointvalue
pointvalue = 0

#define window parameters
win = GraphWin('The Game', 1000,600)
win.yUp()

#define game menu
def begingame():

    startScreen = Rectangle(Point(0,0), Point(1000,600))
    startScreen.setFill('green')
    startScreen.draw(win)

    startMessage1 = Text(Point(500,450), 'A group of INVADERS are trying to steal your gold!')
    startMessage2 = Text(Point(500,375), 'To fight them off, you must click on them before they disappear')
    startMessage3 = Text(Point(500,300), 'To advance to the next level, you must capture at least 8 invaders out of 10')
    startMessage4 = Text(Point(500,100), 'Game will begin in 10 seconds...')

    startMessage1.setTextColor('black')
    startMessage2.setTextColor('black')
    startMessage3.setTextColor('black')
    startMessage4.setTextColor('black')

    startMessage1.setSize(22)
    startMessage2.setSize(16)
    startMessage3.setSize(16)
    startMessage4.setSize(22)

    startMessage1.setStyle('bold')
    startMessage2.setStyle('bold')
    startMessage3.setStyle('bold')
    startMessage4.setStyle('bold')

    startMessage1.draw(win)
    startMessage2.draw(win)
    startMessage3.draw(win)
    startMessage4.draw(win)

    enemies(Point(375,505),win,10)

    
    startScreen.undraw()
    startMessage1.undraw()
    startMessage2.undraw()
    startMessage3.undraw()
    startMessage4.undraw()

    



#Creation of Background
def background():
    # Draw the sky
    sky = Rectangle(Point(0,0), Point(win.getWidth(), win.getHeight()))
    sky.setFill("sky blue")
    sky.draw(win)

    # Draw the dirt
    dirt = Rectangle(Point(0,0), Point(1000, 90))
    dirt.setFill("sienna")
    dirt.draw(win)

    
    # Draw the grass
    grass = Rectangle(Point(0,90), Point(1000,110))
    grass.setFill("sea green")
    grass.draw(win)

    grasspetal1 = Text(Point(500,100), "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    grasspetal1.setSize(36)
    grasspetal1.setStyle("bold")
    grasspetal1.setTextColor("sea green")

    grasspetal2 = grasspetal1.clone()
    grasspetal2.move(15,0)
    
    grasspetal1.draw(win)
    grasspetal2.draw(win)

    # Draw the clouds


    #First Cloud
    cloudbot1 = Oval(Point(425,425), Point(575,475))
    cloudbot1.setFill("white")
    cloudbot1.setOutline("white")

    cloudtop1 = Circle(Point(475,475),25)
    cloudtop1.setFill("white")
    cloudtop1.setOutline("white")

    cloudtop2 = Circle(Point(525,475), 35)
    cloudtop2.setFill("white")
    cloudtop2.setOutline("white")

    cloudbot1.draw(win)
    cloudtop1.draw(win)
    cloudtop2.draw(win)

    #Second Cloud
    cloudbot2 = cloudbot1.clone()
    cloudtop3 = cloudtop1.clone()
    cloudtop4 = cloudtop2.clone()

    cloudbot2.move(-300,-100)
    cloudtop3.move(-300,-100)
    cloudtop4.move(-300,-100)

    cloudbot2.draw(win)
    cloudtop3.draw(win)
    cloudtop4.draw(win)

    #Third Cloud

    cloudbot3 = cloudbot1.clone()
    cloudtop5 = cloudtop1.clone()
    cloudtop6 = cloudtop2.clone()

    cloudbot3.move(250,-100)
    cloudtop5.move(250,-100)
    cloudtop6.move(250,-100)

    cloudbot3.draw(win)
    cloudtop5.draw(win)
    cloudtop6.draw(win)

    #Sun

    sun = Circle(Point(1000,600), 110)
    sun.setFill("orange")
    sun.setOutline("tomato")

    
def hitmarker(x,y,win):
    hitmarker = Text(Point(x,y), 'Hit!')
    hitmarker.setSize(16)
    hitmarker.setTextColor('green')
    hitmarker.draw(win)
    time.sleep(0.5) #DELAY 0.5 SEC
    hitmarker.undraw()
    

def missmarker(x,y,win):
    missmarker = Text(Point(x,y), 'Miss :(')
    missmarker.setSize(16)
    missmarker.setTextColor('red')
    missmarker.draw(win)
    time.sleep(0.5) #DELAY 0.5 SEC
    missmarker.undraw()



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
            
            
            
            
            
            
            
        else:


            pointvalue +=0
            missmarker(x,y,win)
    else:


            pointvalue +=0
            missmarker(x,y,win)
            
            



def nearfriendly(x,y):
    
    global pointvalue

    clickpoint=win.checkMouse()
    
    if clickpoint != None:
        cx = x
        cy = y
        ux = clickpoint.getX()
        uy = clickpoint.getY()
    
        if abs(cx-ux)<=50 and abs(cy-uy)<=50:
            
            pointvalue -=1


            hitmarker(x,y,win)
            
            
            
            
            
            
            
        else:


            pointvalue +=0
            missmarker(x,y,win)
    else:


            pointvalue +=0
            missmarker(x,y,win)
            
            



            
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
    
    time.sleep(delay) #DELAY X SECS
    
    head.undraw()
    eye1.undraw()
    eye2.undraw()
    eyeBrow1.undraw()
    eyeBrow2.undraw()
    mouth.undraw()
    nose.undraw()


#Friendly polygon (LEVEL THREE ONLY)
def friendly(center,win,delay):

    #Friendly head
    head = Circle(center, 25)
    head.setFill('green')
    head.draw(win)

    #Left eye
    eye1Center = center.clone()
    eye1Center.move(-10,5)
    eye1 = Circle(eye1Center,6)
    eye1.setFill('blue')
    eye1.draw(win)

    #Right eye
    eye2center = eye1Center.clone()
    eye2center.move(20,0)
    eye2 = Circle(eye2center,6)
    eye2.setFill('blue')
    eye2.draw(win)

    #Left eyebrow
    eyeBrow1End1 = eye1Center.clone()
    eyeBrow1End1.move(-7,6)
    eyeBrow1End2 = eyeBrow1End1.clone()
    eyeBrow1End2.move(16,2)
    eyeBrow1 = Line(eyeBrow1End1, eyeBrow1End2)
    eyeBrow1.setWidth(3)
    eyeBrow1.draw(win)

    #Right eyebrow
    eyeBrow2End1 = eyeBrow1End2.clone()
    eyeBrow2End1.move(3,0)
    eyeBrow2End2 = eyeBrow2End1.clone()
    eyeBrow2End2.move(16,-6)
    eyeBrow2 = Line(eyeBrow2End1, eyeBrow2End2)
    eyeBrow2.setWidth(3)
    eyeBrow2.draw(win)

    #Mouth
    mouthCorner1 = center.clone()
    mouthCorner1.move(-10,-15)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20,-5)
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill('black')
    mouth.draw(win)

    #Nose
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

        
def levelonewinmenu(pointvalue,win):
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

    time.sleep(5) #DELAY 5 SECONDS

    winmessage.undraw()
    winmessage2.undraw()
    winmessage3.undraw()
    passmessage.undraw()
    lvlonewinback.undraw()



def leveltwomenu(win):

    lvltwomenu = Rectangle(Point(0,0),Point(1000,600))
    lvltwomenu.setFill('grey')
    lvltwomenu.draw(win)

    menumessage = Text(Point(500,500), "In level two the invaders will spawn in at random times.")
    menumessage2 = Text(Point(500,400), "Be quick! Invaders will also disappear faster than in level 1!")
    menumessage3 = Text(Point(500,300), "Again, you need to capture 8 invaders to advance to the next level")
    menumessage4 = Text(Point(500,150), "Level two will begin in 10 seconds...")

    menumessage.setSize(26)
    menumessage.setStyle("bold")
    menumessage.setTextColor('black')
    menumessage.draw(win)

    menumessage2.setSize(24)
    menumessage2.setStyle("bold")
    menumessage2.setTextColor('black')
    menumessage2.draw(win)

    menumessage3.setSize(22)
    menumessage3.setStyle("bold")
    menumessage3.setTextColor('black')
    menumessage3.draw(win)

    menumessage4.setSize(32)
    menumessage4.setStyle("bold")
    menumessage4.setTextColor('black')
    menumessage4.draw(win)

    time.sleep(10)

    lvltwomenu.undraw()
    menumessage.undraw()
    menumessage2.undraw()
    menumessage3.undraw()
    menumessage4.undraw()

def levelthreemenu(win):

    levelthreemenu = Rectangle(Point(0,0),Point(1000,600))
    levelthreemenu.setFill('grey')

    menu2message = Text(Point(500,500), 'In level three there will be green people trying to help you.')
    menu2message.setSize(24)
    menu2message.setStyle("bold")
    menu2message.setTextColor('black')
        
    menu2message2 = Text(Point(500,400), 'Do not click on the friendlies or you will lose 1 point!')
    menu2message2.setSize(24)
    menu2message2.setStyle("bold")
    menu2message2.setTextColor('black')
    
    menu2message3 = Text(Point(500,150), "Level three will begin in 10 seconds...")
    menu2message3.setSize(30)
    menu2message3.setStyle("bold")
    menu2message3.setTextColor('black')

    levelthreemenu.draw(win)
    menu2message.draw(win)
    menu2message2.draw(win)
    menu2message3.draw(win)

    time.sleep(10)

    levelthreemenu.undraw()
    menu2message.undraw()
    menu2message2.undraw()
    menu2message3.undraw()
    

def losemenu(win):
    
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


def leveltwowinmenu(pointvalue):
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
        
def levelone():

    global pointvalue
    pointvalue = 0

    pointcounter = Text(Point(20, 20),pointvalue)
    pointcounter.setSize(18)
    pointcounter.setTextColor('white')
    pointcounter.draw(win)

    time.sleep(1)
      
    for enemyspawn in list(range(10)):


        pointcounter.undraw()

        

        #find random x,y
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        enemies(center,win,1) #random center
        nearenemy(x,y) #nearenemy called


        pointcounter = Text(Point(20, 20),pointvalue)
        pointcounter.setSize(18)
        pointcounter.setTextColor('white')
        pointcounter.draw(win)
        time.sleep(1)
        

        
    pointcounter.undraw()    
        

    if pointvalue >= 8:

        levelonewinmenu(pointvalue,win)

        leveltwomenu(win)

        levelTwo()
        
    else:
        
        losemenu(win)





    
def levelTwo():
    global pointvalue
    pointvalue = 0

    pointcounter = Text(Point(20, 20),pointvalue)
    pointcounter.setSize(18)
    pointcounter.setTextColor('white')
    pointcounter.draw(win)
    time.sleep(1)
    pointcounter.undraw()

    for enemyspawn in list(range(10)):

        #find random x,y
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        time.sleep(random.randrange(1,3))
        enemies(center,win,0.75)
        nearenemy(x,y) #nearenemy called
        pointcounter = Text(Point(20, 20),pointvalue)
        pointcounter.setSize(18)
        pointcounter.setTextColor('white')
        pointcounter.draw(win)
        time.sleep(1)
        pointcounter.undraw()

    pointcounter.undraw()

    if pointvalue >= 8:

        leveltwowinmenu(pointvalue)

        levelthreemenu(win)

        levelthree()
        
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

    global pointvalue
    pointvalue = 0

    # Set the minimum and maximum number of friendlies and enemies
    min_friendlies = 3
    max_friendlies = 7
    min_enemies = 12
    max_enemies = 20

    # Generate a random number of friendlies and enemies within the specified range
    num_friendlies = random.randint(min_friendlies, max_friendlies)
    num_enemies = random.randint(min_enemies, max_enemies)

    # Create the list of friendlies and enemies
    friendlies = ["friendly"  for i in range(1, num_friendlies + 1)]
    enemiesList = ["enemy"  for i in range(1, num_enemies + 1)]

    # Combine the friendlies and enemies into a single list
    characters = friendlies + enemiesList

    # Shuffle the list of characters to put them in a random order
    random.shuffle(characters)

            
    pointcounter = Text(Point(20, 20),pointvalue)
    pointcounter.setSize(18)
    pointcounter.setTextColor('white')
    pointcounter.draw(win)
    time.sleep(1)
    pointcounter.undraw()

    for enemyspawn in characters:

        #find random x,y
        x=random.randint(50,950)
        y=random.randint(50,550)
        center = (Point(x,y))

        time.sleep(random.randrange(1,3))
        if enemyspawn == "friendly":
            friendly(center,win,0.75)
            nearfriendly(x,y)
            print(enemyspawn)
        else:
            enemies(center,win,0.75)
            nearenemy(x,y) #nearenemy called
            print(enemyspawn)
            
        pointcounter = Text(Point(20, 20),pointvalue)
        pointcounter.setSize(18)
        pointcounter.setTextColor('white')
        pointcounter.draw(win)
        time.sleep(1)
        pointcounter.undraw()

    pointcounter.undraw()
    

def main():

    begingame()
    background()
    levelone()

         
main()

#Jason Gupta B03
#jgupta7@gatech.edu; 902983368
#I worked on the homework assignment alone, using only this semester's course materials.
from Myro import *
init("com4")

def danceSing():
    sboytellem()
    wait(.5)
    catdaddy()
    wait(.5)
    sprinkler()
    wait(.5)
    melody()

def menu():

    choice = int(input("1. The Soulja Boy\n 2. The Cat Daddy\n 3. Sprinkler\n 4. Jason's Theme\n 0. Exit\n Which dance step/song would you like?"))
    exitcondition = choice
    while exitcondition != 0:
        if exitcondition == 1:
            sboytellem()
            exitcondition = int(input("1. The Soulja Boy\n 2. The Cat Daddy\n 3. Sprinkler\n 4. Jason's Theme\n 0. Exit\n Which dance step/song would you like?"))
        elif exitcondition == 2:
            catdaddy()
            exitcondition = int(input("1. The Soulja Boy\n 2. The Cat Daddy\n 3. Sprinkler\n 4. Jason's Theme\n 0. Exit\n Which dance step/song would you like?"))
        elif exitcondition == 3:
            sprinkler()
            exitcondition = int(input("1. The Soulja Boy\n 2. The Cat Daddy\n 3. Sprinkler\n 4. Jason's Theme\n 0. Exit\n Which dance step/song would you like?"))
        elif exitcondition == 4:
            melody()
            exitcondition = int(input("1. The Soulja Boy\n 2. The Cat Daddy\n 3. Sprinkler\n 4. Jason's Theme\n 0. Exit\n Which dance step/song would you like?"))
        else:
            print("I'm sorry I don't know that one.")
            exitcondition = int(input("1. The Soulja Boy\n 2. The Cat Daddy\n 3. Sprinkler\n 4. Jason's Theme\n 0. Exit\n Which dance step/song would you like?"))
    print("Have a good day!")
def sboytellem():
    i = 0
    while i < 2:
        for a in timer(1):
            motors(.2, .4)
        for b in timer(1):
            motors(-.2, -.4)
        i = i + 1
    ind = 0
    while ind < 2:
        for c in timer(1):
            motors(.4, .2)
        for d in timer(1):
            motors(-.4, -.2)
        ind = ind + 1
     #yooooooooo
    turnLeft(1, .75)
    backward(.5, 3)
    turnRight(1, 1.5)
    backward(.5,3)
    turnLeft(1, 1.5)
    backward(.5,3)
    turnRight(1,1.5)
    backward(.5,3)

    turnLeft(1,.75)
    index = 0
    while index < 2:
        for e in timer(1):
            motors(.2, .4)
        for f in timer(1):
            motors(-.2, -.4)
        index = index + 1
    lit = 0
    while lit < 2:
        for g in timer(1):
            motors(.4, .2)
        for h in timer(1):
            motors(-.4, -.2)
        lit = lit + 1

    #superman!
    turnLeft(.3,.5)
    forward(.6,2)
    backward(.6,2)
    turnRight(.3,.5)
    #yoooooooooooo
    turnLeft(1, .75)
    backward(.5, 3)
    turnRight(1, 1.5)
    backward(.5,3)
    turnLeft(1, 1.5)
    backward(.5,3)
    turnRight(1,1.5)
    backward(.5,3)
    #reposition
    turnLeft(1, .75)

def catdaddy():
    repeat = 0
    while repeat < 2:
        for t in timer(1):
            motors(0, -.5)
        for x in timer(1.5):
            motors(0,.5)
        forward(.8, 2)
        backward(.8, 2)
        for w in timer(1):
            motors(-.5, 0)
        for e in timer(1.5):
            motors(.5,0)
        forward(.8, 2)
        backward(.8, 2)
        i = 0
        while i < 2:
            for a in timer(1):
                motors(.2, .5)
            for b in timer(1):
                motors(-.2, -.5)
            i = i + 1
        repeat = repeat + 1
    stop()
def sprinkler():

    turnLeft(.5,3)
    i = 0
    while i < 3:
        turnRight(.5, .5)
        i = i + .5
    #now other side

    wait(.5)
    turnRight(.5, 3)
    s = 0
    while s < 3:
        turnLeft(.5, .5)
        s = s + .5

def melody():

    i = 0
    index = 0
    while index < 3:
        while i < 4:
            beep(.25, 1500)
            beep(.25, 1500)
            beep(.5, 1000)
            i = i + 1
            beep(1, 1000)
            beep(.25, 800)
            beep(1, 1000)
            beep(.25, 800)
        index = index + 1

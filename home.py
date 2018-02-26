# -*- coding: utf-8 -*-
import Tkinter as tk
from random import randint
from Bestiary import *
import math

root = tk.Tk()

#Initialize the game interface
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.grid(row=0, column=0)
text = tk.Canvas(root, height=500, width=500, bg="white")
text.grid(row=0, column=1)
statBar = tk.Canvas(root, height=200, width=500, bg="white")
statBar.grid(row=1, column=1)
pos = [randint(1,23), randint(1,23)]    #Generate random start position
player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
board = []

#Set position of doors in each room
rooms = [[[-1], [[False,False,True,False],1], [-1]],[[[False,False,True,True],1], [[True,True,True,True],1], [[False,True,True,False],1]],[[[True,False,False,True],1], [[True,True,True,True],1], [[True,True,False,False],1]],[[-1],[[True,False,False,False],1],[-1]]]

#Set basic statistics
c = [3,1,-20]    #X-Room, Y-Room, Line on which to display text
cover = None
pl = Player()
box = None
pl.sugar = 0

#Initialize board and interface in tkinter
for i in range(1, 24):
    canvas.create_line(0, 20*i, 500, 20*i, fill="black")
    canvas.create_line(20*i, 0, 20*i, 500, fill="black")

#Represent board as a 2D array
for i in range(0,25):
    board.append([])
    for j in range(0,25):
        board[i].append(0)

#Add walls at edges of square board
canvas.create_rectangle(0, 0, 20, 500, fill="black")
canvas.create_rectangle(0, 0, 500, 20, fill="black")
canvas.create_rectangle(0, 480, 500, 500, fill="black")
canvas.create_rectangle(480, 0, 500, 500, fill="black")

#Set position of first door
board[12][0] = 1
doors = [canvas.create_rectangle(240, 0, 260, 20, fill="blue")]

#Initialize enemies and game condition
en = []
enPos = []
game = True
     
def drawPlayer():
    '''This function draws a player at the position given by pos'''
    global player
    global c
    f = "green"
    if c[0] == 1 and c[1] == 1 and pl.inv[3] <= 0:
        f = "black"         #If room is dark, display player as black so it can't be seen
    canvas.delete(player)   #Delete existing player circle to replace it    
    player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill=f) #Draw new player
    
def drawEnemy(x,y,num):
    '''Draw enemy at index num in the en array at given position (x,y)'''
    global en
    global c
    f = "red"
    
    #Based on the room, change the color of the enemies
    if c[0] == 1 and c[1] == 1 and pl.inv[3] <= 0:
        f = "black"
    elif c[0] == 1 and c[1] == 0:
        f = "orange"          
    elif c[0] == 1 and c[1] == 1:
        f = "brown"
    elif c[0] == 1 and c[1] == 2:
        f = "black"          
    elif c[0] == 2 and c[1] == 0:
        f = "forestgreen"           
    elif c[0] == 2 and c[1] == 1:
        f = "aquamarine"
    elif c[0] == 2 and c[1] == 2:
        f = "grey"        
    elif c[0] == 3 and c[1] == 1:
        f = "red"    
        
    #If final boss (65), draw a circle occupying 9 squares, otherwise, draw a red square defined by en[num]
    if num == 65:
        canvas.delete(en[0])
        en[0] = canvas.create_oval(20*x, 20*y, 20*(x+3), 20*(y+3), fill="red")
    elif num == len(en):
        en.append(canvas.create_oval(20*x, 20*y, 20*(x+1), 20*(y+1), fill=f))
    elif num > len(en):
        pass
    else:
        canvas.delete(en[num])
        en[num] = canvas.create_oval(20*x, 20*y, 20*(x+1), 20*(y+1), fill=f)

drawPlayer()    #initialize player

def enemies():
    '''Draw all enemies in a given room given the room defined by c[0] and c[1]'''
    global enPos
    global en
    global board
    
    #Delete all existing enemies from previous room
    while len(enPos) > 0:
        del enPos[0]
        del en[0]
        
    #In any room except the final boss room, generate enemies given by a type of scientist
    if c[0] != 0:
        for i in range(0,5):
            if len(enPos) < 5:
                if c[0] == 1 and c[1] == 0:
                    enPos.append(Mathematician(rooms[c[0]][c[1]][1]))
                if c[0] == 1 and c[1] == 1:
                    enPos.append(Geologist(rooms[c[0]][c[1]][1]))
                if c[0] == 1 and c[1] == 2:
                    enPos.append(Astronomer(rooms[c[0]][c[1]][1]))
                if c[0] == 2 and c[1] == 0:
                    enPos.append(Biologist(rooms[c[0]][c[1]][1]))
                if c[0] == 2 and c[1] == 1:
                    enPos.append(Chemist(rooms[c[0]][c[1]][1]))
                if c[0] == 2 and c[1] == 2:
                    enPos.append(Physicist(rooms[c[0]][c[1]][1]))
                if c[0] == 3 and c[1] == 1:
                    enPos.append(Enemy(rooms[c[0]][c[1]][1]))
            enPos[i].updatePos(randint(1,23), randint(1,23))        #Generate start enemy position
            while enPos[i][0] == pos[0] and enPos[i][1] == pos[1]:  #Make sure en position is not player position
                enPos[i] = [randint(1,23), randint(1,23)]
            drawEnemy(enPos[i][0], enPos[i][1], i)
            board[enPos[i][0]][enPos[i][1]] = (i+2)                 #Give every enemy an identifying number in the board array
            
    #Final boss room
    else:
        #Initialize Rick Perry, the fearsome final foe
        en.append(canvas.create_oval(220,60,280,120,fill="red"))
        enPos.append(RickPerry())
        enPos[0].updatePos(11,3)
        for i in range(0,3):    #Set all 9 squares to the number 2 to identify Rick Perry
            for j in range(0,3):
                board[enPos[0][0]+i][enPos[0][1]+j] = 2
        drawEnemy(enPos[0][0],enPos[0][1],65)
        
enemies()   #Initialize enemies

def newRoom():
    '''Every time a player enters a new room, initialize boxes, enemies, etc. Uses the global variables doors, rooms, en, cover, box, and board to determine room conditions'''
    global doors
    global rooms
    global en
    global cover
    global box
    global board
    
    #If exiting a dark room, remove the darkness; let there be light!
    if cover != None:
        canvas.delete(cover)
        cover = None
        
    #If a box existed, delete the box
    if box != None:
        canvas.delete(box[0])
        board[box[1]][box[2]] = 0
        box = None
    q = 0
    temp = [0,0]
    
    #Delete all existing doors and enemies so they don't reappear in new room
    for door in doors:
        canvas.delete(door)
    for enemy in en:
        canvas.delete(enemy)
        
    #Based on rooms array, draw the doors in the room with math that works
    for i in range(0,4):
        jeff = [[12,0,12,24],[0,12,24,12]]
        z = i
        if i>=2:
            q = 480
            z = i-2
            temp = [480,480,480,480]
        if rooms[c[0]][c[1]][0][i]:
            temp[z] = 240
            if c[0] == 1 and c[1] == 1 and pl.inv[2] == 0 and i == 0:
                doors.append(canvas.create_rectangle(temp[0], temp[1], temp[0]+20, temp[1]+20, fill="orange")) 
            else:
                doors.append(canvas.create_rectangle(temp[0], temp[1], temp[0]+20, temp[1]+20, fill="blue"))
            temp[z] = q
            board[jeff[0][i]][jeff[1][i]] = 1
        else:
            board[jeff[0][i]][jeff[1][i]] = 0
            
    #If you're exiting Rick Perry's room, clear all the markers in board array
    if len(enPos) > 0 and enPos[0].name == "Rick Perry":
        for i in range(0,3):
            for j in range(0,3):
                board[enPos[0][0]+i][enPos[0][1]+j] = 0           
    else: #Otherwise, clear all enemy fields
        for i in range(0,len(enPos)):
            board[enPos[i][0]][enPos[i][1]] = 0
            
    enemies()   #Generates new enemies
    if c[0] == 1 and c[1] == 1 and pl.inv[3] <= 0:  #If entering dark room without light source, it must be dark
        cover = canvas.create_rectangle(0,0,500,500, fill="black")  #Cover makes the room dark by drawing a black square
    elif c[:2] != [0,1]:                #Create a box if not in Rick Perry's room
        q = [randint(1,23), randint(1,23)]
        while q == pos or board[q[0]][q[1]] >= 1:   #Box Position should not be player pos or enemy pos
            q = [randint(1,23), randint(1,23)]
        box = [canvas.create_rectangle(q[0]*20, q[1]*20, (q[0]+1)*20, (q[1]+1)*20, fill="brown"),q[0],q[1]]
        board[q[0]][q[1]] = -1

    if pl.inv[10]:
        ret = "Entering the level " + str(rooms[c[0]][c[1]][1]) + " "
        if c[0] == 1 and c[1] == 0:
            ret += "numbers"
        if c[0] == 1 and c[1] == 1:
            ret += "rocks"
        if c[0] == 1 and c[1] == 2:
            ret += "SPAAAAAAAAACE"
        if c[0] == 2 and c[1] == 0:
            ret += "plants"
        if c[0] == 2 and c[1] == 1:
            ret += "chemiscry"
        if c[0] == 2 and c[1] == 2:
            ret += "feejyx"
        if c[0] == 3 and c[1] == 1:
            ret += "'General Science'"
        addText(ret + " room")
    else:
        if c[0] == 1 and c[1] == 0:
            addText("The math room. Dr. Eng peers at you from his corner.")
        if c[0] == 1 and c[1] == 1 and pl.inv[3]==0:
            addText("It’s pitch black. This is the Geologist cave.")
        if c[0] == 1 and c[1] == 1 and pl.inv[3]==1:
            addText("You enter the geology room. Who studies rocks, anyways?")
        if c[0] == 1 and c[1] == 2:
            addText("We don’t even have a astronomy class. Whatever. SPAACE.")
        if c[0] == 2 and c[1] == 0:
            addText("You enter the bio room. Wisconsin Fast Plants are everywhere.")
        if c[0] == 2 and c[1] == 1:
            addText("You enter the chem room. There's a pile of failed-postlabs.")
        if c[0] == 2 and c[1] == 2:
            addText("You enter the physics room. Whiteboards are everywhere.")
        if c[0] == 3 and c[1] == 1:
            addText("Back to the MPR. Lots of Scibowlers are here.")
        if c[0] == 0 and c[1] == 1:  
            addText("Scibowl Nats. Only Rick Perry (and blurts) can stop you now.")
def endGame():
    '''Displays green text on black background describing the end result, either "Game Over" or "You win!". This function only activates if the Boolean variable game has a value of false'''
    txt = None
    if pl.hp <= 0:          #If player is dead, game is over
        txt = "Game Over!"
    else:                   #Otherwise, you win!!!
        txt = "You win!" 
        
    #Clear everything from the canvas, and display end message
    canvas.delete("all")
    canvas.create_rectangle(0,0,500,500,fill="black")
    canvas.create_text(230,230,anchor="nw",text=txt, fill="green")        
                        
def attackPlayer(num):
    '''Enemy given by enPos[num] attacks player and deals damage'''
    global game
    addText("Was " + enPos[num].attack + " by " + enPos[num].name + " dealing " + str(pl.attacked(enPos[num].knowledge)) + " damage.")  #Display damage dealt to player
    
    if pl.hp <= 0:  #At player death, display message and trigger endGame() by setting game to False
        addText("You died!")
        pl.hp = 0
        game = False
    
def attackEnemy(num):
    '''Player attacks an enemy given by enPos[num] and deals damage to enemy and gains experience'''
    global game
    global board
    addText("Dealt "+str(enPos[num].attacked(pl.knowledge,1))+" damage to "+enPos[num].name)    #Display damage dealt to enemy  
    if pl.sugar > 0:    #Player loses sugar if player had sugar
        addText("You feel a little woozy...")
        pl.knowledge = pl.knowledge/(2*(2**(pl.sugar-1)))
        pl.sugar = 0

    if enPos[num].hp <= 0:  #If an enemy dies, delete the enemy and player gains dropped xp
        pl.giveXP(enPos[num].xp)
        updateStats()
        addText(enPos[num].name+" died!")
        canvas.delete(en[num])
        board[enPos[num][0]][enPos[num][1]] = 0
        if enPos[num].name == "Rick Perry": #If the killed enemy was Rick Perry, the endGame() function is triggered
            game = False
        del enPos[num]
        del en[num]
        
    if len(enPos) < 5:
        rooms[c[0]][c[1]][1] += 1   #Increase enemy level the next time the room is entered
    
  
def stuffHappens(jeff):
    '''This function defines the movement of all enemies and the player. It takes one argument:
        jeff - an array in the format [x,y] which describes the player's movement using the numbers -1, 0, and 1'''
    global pos
    global enPos
    global board
    global c
    oldPos = [pos[0]-jeff[0], pos[1]-jeff[1]]   #Calculate a player's old position using the change given by jeff
    
    if not game:    #Catch movement if game has ended
        addText("The game is over, nice try")
    else:
        if c[0] == 1 and c[1] == 1 and pos == [12,0] and (pl.inv[2] <= 0 or False in pl.inv[4:]):
            if pl.inv[2] <= 0:    #If the player attempts to move through a locked door without a key, deny them
                addText("That door is locked, dingus")
            elif False in pl.inv[4:]:
                addText("The key clicks, but the door does not budge")
                addText("Perhaps you should open more boxes")
            pos = oldPos 
        elif pos[0] <= 0:   #All cases for a player moving back through a door; generates new room and changes c based on which room the user enters
            if pos[1] == oldPos[1]:
                c[1] -= 1
                newRoom()
                pos[0] = 24
        elif pos[0] >= 24:
            if pos[1] == oldPos[1]:
                c[1] += 1
                newRoom()
                pos[0] = 0
        elif pos[1] <= 0:
            if pos[0] == oldPos[0]:
                c[0] -= 1
                newRoom()
                pos[1] = 24
        elif pos[1] >= 24:
            if pos[0] == oldPos[0]:
                c[0] += 1
                newRoom()
                pos[1] = 0
        elif board[pos[0]][pos[1]] >= 2 or (board[pos[0]][pos[1]] <= -2 and board[pos[0]][pos[1]] >= -6): #The player attacks an enemy
            if pl.inv[9] and randint(1,4) == 1: #if player has a seismograph, 25% chance of causing earthquake
                addText("Earthquake!")
                l = len(enPos)
                for i in range(l):
                    attackEnemy(l-i-1)
            elif pl.inv[8]: #if player has a compass
                diff = [pos[0]-oldPos[0],pos[1]-oldPos[1]]
                around = [board[oldPos[0]+diff[0]][oldPos[1]+diff[1]],
                          board[oldPos[0]+diff[1]][oldPos[1]-diff[0]],
                          board[oldPos[0]-diff[0]][oldPos[1]-diff[1]],
                          board[oldPos[0]-diff[1]][oldPos[1]+diff[0]]]
                for i in sorted(around)[::-1]: #check every tile around player
                    if i > 0: attackEnemy(i-2) #attack if tile has an enemy
            else: attackEnemy(abs(board[pos[0]][pos[1]])-2) #Attack enemy, consequences and results shown in attackEnemy() function
            pos = oldPos
        drawPlayer()
    
        #Rick Perry's automated moves with respect to the center of his circle of radius 1.5 squares.
        if len(enPos) > 0 and enPos[0].name == "Rick Perry":
            cen = [enPos[0][0]+1, enPos[0][1]+1]
            #Calculate difference in x distance and y distance to player
            dx = cen[0] - pos[0]
            dy = cen[1] - pos[1]
            newX = cen[0]
            newY = cen[1]
            #Advance in the direction with greater difference
            if abs(dx) > abs(dy):
                newX = cen[0] - int(dx/abs(dx))
            elif abs(dy) > abs(dx):
                newY = cen[1] - int(dy/abs(dy))
            elif randint(0,1) == 0:
                newX = cen[0] - int(dx/abs(dx))
            else:
                newY = cen[1] - int(dy/abs(dy))
            if newX-1 <= 0 or newX+1 >= 25 or newY-1 <= 0 or newY+1 >= 25:
                newX = cen[0]
                newY = cen[1]
            elif abs(newX-pos[0]) <= 1 and abs(newY-pos[1]) <= 1:
                newX = cen[0]
                newY = cen[1]
                attackPlayer(0)
            #Replace 0's with 2 in board to identify enemy
            for i in range(0,3):
                for j in range(0,3):
                    board[enPos[0][0]+i][enPos[0][1]+j] = 0
                    board[newX-1+i][newY-1+j] = 2
            enPos[0].updatePos((newX-1),(newY-1))
            drawEnemy(enPos[0][0], enPos[0][1], 65)    
        else:   #Do the same thing as above, but with only one square instead of 9
            for i in range(0,len(enPos)):
                dx = enPos[i][0] - pos[0]
                dy = enPos[i][1] - pos[1]
                newX = enPos[i][0]
                newY = enPos[i][1]
                if abs(dx) > abs(dy):
                    newX = enPos[i][0] - int(dx/abs(dx))
                elif abs(dy) > abs(dx):
                    newY = enPos[i][1] - int(dy/abs(dy))
                elif randint(0,1) == 0:
                    newX = enPos[i][0] - int(dx/abs(dx))
                else:
                    newY = enPos[i][1] - int(dy/abs(dy))   
                if abs(board[newX][newY]) >= 2 or newX <= 0 or newX >= 24 or newY >= 24 or newY <= 0:
                    newX = enPos[i][0]
                    newY = enPos[i][1]
                elif newX == pos[0] and newY == pos[1]:
                    attackPlayer(i)
                    newX = enPos[i][0]
                    newY = enPos[i][1]
                #If this square was originally a box, restore the box
                if board[enPos[i][0]][enPos[i][1]] < 0:
                    board[enPos[i][0]][enPos[i][1]] = -1
                else:
                    board[enPos[i][0]][enPos[i][1]] = 0
                
                if board[newX][newY] == 0:
                    board[newX][newY] = i+2 
                else:
                    board[newX][newY] = -(i+2)  
                enPos[i].updatePos(newX, newY)
                drawEnemy(enPos[i][0], enPos[i][1], i)

        if pl.inv[5] and len(enPos) > 0: pl.hp = min(pl.maxhp,pl.hp+1)
        
        updateStats()
    if not game:    #if game is false, end the game
        endGame()   
    
def addText(txt):
    '''Add the text given by the variable txt to the main output screen; takes one argument:
        txt - Text to be outputted as a string'''
    if c[2] == 480: #Reset the canvas if it is full
        text.delete("all")
        c[2] = 0
    else:
        c[2] += 20
    text.create_text(2,c[2],text=txt,anchor='nw',font=('Courier',10))
  
addText('Hello there! Welcome to the world of SciBowl!\n')
addText('My name is Tracey! People call me the SciBowl Prof!\n')
addText('This world is inhabited by creatures called Scibowlers!\n')
addText('For some people, SciBowlers are students. Others use \n')
addText('them for fights. Myself...I study SciBowl as a profession.\n')
addText('Now, what is your name...?\n')
addText('')
addText('')
addText('')
addText('Ha! You thought you had a choice?\n')
addText('Your name is Linnaeus. Linnaeus! Your very own SciBowl \n')
addText('legend is about to unfold! A world of dreams and \n')
addText('adventures with SciBowl awaits!"')

def updateStats():
    '''Update the stats canvas to show the most recent stats'''
    statBar.delete("all")
    #Display stats with most recent player values
    statBar.create_text(0,0,text=" Player Stats"+
    "\n Level: "+str(pl.level)+
    "\n HP: "+str(pl.hp) + "/" +str(pl.maxhp)+
    "\n Knowledge (Attack): "+str(pl.knowledge)+  
    "\n Immunity (Defense): "+str(pl.immune)+
    "\n XP: "+str(pl.xp)+"/"+str(10*pl.level**2),
    anchor='nw',font=('Courier',10))

def left():
    '''On a left key or left button event, activate this function'''
    global pos
    if (pos[0] <= 1 and board[0][pos[1]] == 0) or (pos[1] == 0 or pos[1] == 24):    #Do not allow player to walk through walls
        addText("You have now reached peak neoliberalism.")
    else:
        pos[0] -= 1
    stuffHappens([-1,0])
    
def right():
    '''On a right key or right button event, activate this function'''
    global pos
    if (pos[0] >= 23 and board[24][pos[1]] == 0) or (pos[1] == 0 or pos[1] == 24):  #D not allow player to walk through walls
        addText("Is this the right way?")
    else:
        pos[0] += 1
    stuffHappens([1,0])
    
def up():
    '''On an up key or up button event, activate this function'''
    global pos
    if (pos[1] <= 1 and board[pos[0]][0] == 0) or (pos[0] == 0 or pos[0] == 24):    #Do not allow player to walk through walls
        addText("Y'all are just so uppity!")
    else:
        pos[1] -= 1
    stuffHappens([0,-1])
    
def down():
    '''On a down key or down button event, activate this function'''
    global pos
    if (pos[1] >= 23 and board[pos[0]][24] == 0) or (pos[0] == 0 or pos[0] == 24):  #Do not allow player to walk through walls
        addText("Dude, I LOVE walls!!!")
    else:
        pos[1] += 1
    stuffHappens([0,1])
    
#Shell functions for each button event to discard the event passed by <Key>
def hi(key):
    up()
    
def hi2(key):
    down()
    
def hi3(key):
    left()
    
def hi4(key):
    right()
    
def interact():
    '''Interacting with boxes results in this function, which will give you various objects based on a random number'''
    global board
    if board[pos[0]][pos[1]] == -1:
        q = randint(0,10)   #Generate random number
        if q == 0:          #1/11 chance
            pl.inv[2] += 1
            addText("You gained a key. Door unlocked!")     #Needed to unlock door
            updateStats()
        elif q == 1:        #1/11 chance
            pl.inv[3] += 1
            addText("You have gained a lamp. Let there be light")   #Needed to make room light
            updateStats()
        elif q == 2 or q == 3:  #2/11 chance
            pl.inv[1] += 1
            addText("You got some C6H1206 (glucose). Sweet!")
            if pl.inv[1] > 5: #bag is overflowing with sugar
                pl.inv[1] = 5
                addText("You don't have enough space to carry so much sugar!")
        elif q >=4 and q<=7:    #4/11 chance
            r = randint(1,3)
            pl.inv[0] += r
            if r == 1:
                addText("You have gained 1 health potion.")
            else:
                addText("You have gained " + str(r) + " health potions.")
            if pl.inv[0] > 10: #bag is overflowing with potions
                pl.inv[0] = 10
                addText("You don't have enough space to carry so many potions!")
        else:               #3/11 chance
            if c[0] == 3 and c[1] == 1 and not pl.inv[4]:
                addText("You got a textbook!")
                addText("Knowledge has permanently increased by 10")
                pl.inv[4] = True
                pl.knowledge += 10
            elif c[0] == 2 and c[1] == 0 and not pl.inv[5]:
                addText("You got a chloroplast!")
                addText("HP will regenerate naturally")
                pl.inv[5] = True
            elif c[0] == 2 and c[1] == 1 and not pl.inv[6]:
                addText("You got a distiller!")
                addText("Potions now heal double")
                pl.inv[6] = True
            elif c[0] == 2 and c[1] == 2 and not pl.inv[7]:
                addText("You got a mirror!")
                addText("Immune has permanently increased by 6")
                pl.inv[7] = True
                pl.immune += 6
            elif c[0] == 1 and c[1] == 0 and not pl.inv[8]:
                addText("You got a compass!")
                addText("Attacks will do damage in all directions")
                pl.inv[8] = True
            elif c[0] == 1 and c[1] == 1 and not pl.inv[9]:
                addText("You got a seismograph!")
                addText("Attacks have a chance to deal damage to all enemies in the room")
                pl.inv[9] = True
            elif c[0] == 1 and c[1] == 2 and not pl.inv[10]:
                addText("You got a star chart!")
                addText("Room levels are now revealed")
                pl.inv[10] = True
            else:
                addText("This box has nothing, because we're mean")
        board[pos[0]][pos[1]] = -65     #You can't open open boxes
    elif board[pos[0]][pos[1]] == -65:
        addText("Again? Seriously?")
    else:   #You can't open nonexistent boxes
        addText("Nothing to see here...")
    updateStats()
        
def potion():
    '''Allows the user to drink a tacky red potion to regain health'''
    if pl.inv[0] > 0:   #If player has potions in stock, allow use of one
        pl.inv[0] -= 1
        addText("An awfully tacky red potion. You drink it.")
        if pl.inv[6]: pl.hp = min(pl.hp+20,pl.maxhp)
        else: pl.hp = min(pl.hp+10,pl.maxhp)
        updateStats()
    else:   #Otherwise, no soup for you.
        addText("No soup for you!")
    updateStats()

def sugar():
    '''Allow the player to eat sugar, giving a temporary energy boost'''
    if pl.inv[1] <= 0:  #Can't use it if you don't have it
        addText( "No more Skittles for you.")
        pl.inv[1] = 0
    else:               #Increase the next attack
        pl.inv[1] -= 1
        addText("An oncoming sugar rush has increased your next attack!")
        pl.sugar +=1
        pl.knowledge = pl.knowledge*2
    updateStats()

def backpack():
    '''Display the elements in the backpack (player's inventory)'''
    statBar.delete("all")   #Delete all stats from stats menu
    item = ""
    #Display quantity of all items
    if pl.inv[2]>=1 or pl.inv[3]>=1 or pl.inv[4]>=1 or pl.inv[5]>=1 or pl.inv[6] or pl.inv[7]>=1 or pl.inv[8]>=1 or pl.inv[9]>=1 or pl.inv[10]>=1:
        item += " Supercritical Items:\n"    
        if pl.inv[2] >= 1:
            item += " Mysterious Key: Seems to unlock a door.\n"
        if pl.inv[3] >= 1:
            item += " Oil Lamp: Lights up dark rooms.\n"
        if pl.inv[4] >= 1:
            item += " Textbook: Flat knowledge boost.\n"
        if pl.inv[5] >= 1:
            item += " Chloroplast: Health regens over time.\n"
        if pl.inv[6] >= 1:
            item += " Distiller: % boost for health potions.\n"
        if pl.inv[7] >= 1:
            item += " Mirror: Flat immunity boost.\n"
        if pl.inv[8] >= 1:
            item += " Compass: Attacks do AOE damage.\n"
        if pl.inv[9] >= 1:
            item += " Seismograph: Chance to damage all enemies.\n"
        if pl.inv[10] >= 1:
            item += " Star Chart: Displays level of room.\n"
    if pl.inv[0] >= 1 or pl.inv[1]>=1:
        item += "\n Consumables:\n"
        if pl.inv[0] >= 1:
            item += " Health Potion (x" + str(pl.inv[0]) + "): Heals flat HP.\n"
        if pl.inv[1] >= 1:
            item += " Sugar (x" + str(pl.inv[1]) + "): Doubles attack for 1 turn.\n"
    statBar.create_text(0,0,text=
    " Backpack \n\n" + str(item),
    anchor='nw',font=('Courier',8))

#Add events to each key to allow use of keyboard
root.bind("<Up>", hi)
root.bind("<Down>", hi2)
root.bind("<Left>", hi3)
root.bind("<Right>", hi4)

#Add a frame as well as each button to the frame
frame = tk.Frame(root)
tk.Button(frame, text="Left", command=left).grid(row=1, column=0, columnspan=2)
tk.Button(frame, text="Right", command=right).grid(row=1, column=2, columnspan=2)
tk.Button(frame, text="Up", command=up).grid(row=0, column=1, columnspan=2)
tk.Button(frame, text="Down", command=down).grid(row=2, column=1, columnspan=2)
tk.Button(frame, text="Interact", command=interact).grid(row=0, column=5)
tk.Button(frame, text="Health Potion", command = potion).grid(row=1, column=5)
tk.Button(frame, text="Eat Sugar", command = sugar).grid(row=2, column=5)
tk.Button(frame, text="Backpack", command = backpack).grid(row=0, column=6)
tk.Button(frame, text="Player Stats", command = updateStats).grid(row=1, column=6)

#Add the frame to the grid, initialize stats
frame.grid(row=1,column=0, columnspan=1)
updateStats()
    
#Display all content
root.mainloop()

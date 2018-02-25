import tkinter as tk
from random import randint
from Bestiary import *
import math

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.grid(row=0, column=0)
text = tk.Canvas(root, height=500, width=500, bg="white")
text.grid(row=0, column=1)
statBar = tk.Canvas(root, height=200, width=500, bg="white")
statBar.grid(row=1, column=1)
pos = [randint(1,23), randint(1,23)]
player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
board = []
rooms = [[[-1], [False,False,True,False], [-1]],[[False,False,True,True], [True,True,True,True], [False,True,True,False]],[[True,False,False,True], [True,True,True,True], [True,True,False,False]],[[-1],[True,False,False,False],[-1]]]
c = [3,1,-20]
cover = None
pl = Player()
box = None
pl.sugar = 0

for i in range(1, 24):
    canvas.create_line(0, 20*i, 500, 20*i, fill="black")
    canvas.create_line(20*i, 0, 20*i, 500, fill="black")

for i in range(0,25):
    board.append([])
    for j in range(0,25):
        board[i].append(0)
   
canvas.create_rectangle(0, 0, 20, 500, fill="black")
canvas.create_rectangle(0, 0, 500, 20, fill="black")
canvas.create_rectangle(0, 480, 500, 500, fill="black")
canvas.create_rectangle(480, 0, 500, 500, fill="black")

board[12][0] = 1
doors = [canvas.create_rectangle(240, 0, 260, 20, fill="blue")]
en = []
enPos = []
game = True
     
def drawPlayer():
    global player
    global c
    f = "green"
    if c[0] == 1 and c[1] == 1 and pl.inv[3] <= 0:
        f = "black"
    canvas.delete(player)
    player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill=f)
    
def drawEnemy(x,y,num):
    global en
    global c
    f = "red"
    if c[0] == 1 and c[1] == 1 and pl.inv[3] <= 0:
        f = "black"
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

drawPlayer()

def enemies():
    global enPos
    p = len(enPos)
    for i in range(0, p):
        del enPos[0]
        del en[0]
    if c[0] != 0:
        for i in range(0,5):
            if len(enPos) < 5:
                if c[0] == 1 and c[1] == 0:
                    enPos.append(Mathematician(1))
                if c[0] == 1 and c[1] == 1:
                    enPos.append(Geologist(1))
                if c[0] == 1 and c[1] == 2:
                    enPos.append(Astronomer(1))
                if c[0] == 2 and c[1] == 0:
                    enPos.append(Biologist(1))
                if c[0] == 2 and c[1] == 1:
                    enPos.append(Chemist(1))
                if c[0] == 2 and c[1] == 2:
                    enPos.append(Physicist(1))
                if c[0] == 3 and c[1] == 1:
                    enPos.append(Enemy(1))
            enPos[i].updatePos(randint(1,23), randint(1,23))
            while enPos[i][0] == pos[0] and enPos[i][1] == pos[1]:
                enPos[i] = [randint(1,23), randint(1,23)]
            drawEnemy(enPos[i][0], enPos[i][1], i)
            board[enPos[i][0]][enPos[i][1]] = (i+2)
            
    else:
        en.append(canvas.create_oval(220,60,280,120,fill="red"))
        enPos.append(RickPerry())
        enPos[0].updatePos(11,3)
        for i in range(0,3):
            for j in range(0,3):
                board[enPos[0][0]+i][enPos[0][1]+j] = 2
        drawEnemy(enPos[0][0],enPos[0][1],65)
        
enemies()

def newRoom():
    global doors
    global rooms
    global en
    global cover
    global box
    if cover != None:
        canvas.delete(cover)
        cover = None
    if box != None:
        canvas.delete(box[0])
        board[box[1]][box[2]] = 0
        box = None
    q = 0
    temp = [0,0]
    for door in doors:
        canvas.delete(door)
    for enemy in en:
        canvas.delete(enemy)
    for i in range(0,4):
        jeff = [[12,0,12,24],[0,12,24,12]]
        z = i
        if i>=2:
            q = 480
            z = i-2
            temp = [480,480,480,480]
        if rooms[c[0]][c[1]][i]:
            temp[z] = 240
            if c[0] == 1 and c[1] == 1 and pl.inv[2] == 0 and i == 0:
                doors.append(canvas.create_rectangle(temp[0], temp[1], temp[0]+20, temp[1]+20, fill="orange")) 
            else:
                doors.append(canvas.create_rectangle(temp[0], temp[1], temp[0]+20, temp[1]+20, fill="blue"))
            temp[z] = q
            board[jeff[0][i]][jeff[1][i]] = 1
        else:
            board[jeff[0][i]][jeff[1][i]] = 0
    if len(enPos) > 0 and enPos[0].name == "Rick Perry":
        for i in range(0,3):
            for j in range(0,3):
                board[enPos[0][0]+i][enPos[0][1]+j] = 0           
    else:
        for i in range(0,len(en)):
            board[enPos[i][0]][enPos[i][1]] = 0
    enemies()
    if c[0] == 1 and c[1] == 1 and pl.inv[3] <= 0:
        cover = canvas.create_rectangle(0,0,500,500, fill="black")
    elif c[:2] not in [[0,1],[1,1]]:
        q = [randint(1,23), randint(1,23)]
        while q == pos or board[q[0]][q[1]] >= 1:
            q = [randint(1,23), randint(1,23)]
        box = [canvas.create_rectangle(q[0]*20, q[1]*20, (q[0]+1)*20, (q[1]+1)*20, fill="brown"),q[0],q[1]]
        board[q[0]][q[1]] = -1

def endGame():
    txt = None
    if pl.hp == 0:
        txt = "Game Over!"
    else:
        txt = "You win!" 
    canvas.delete("all")
    canvas.create_rectangle(0,0,500,500,fill="black")
    canvas.create_text(230,230,anchor="nw",text=txt, fill="green")        
                        
def attackPlayer(num):
    global game
    addText("Was " + enPos[num].attack + " by " + enPos[num].name + " dealing " + str(pl.attacked(enPos[num].knowledge)) + " damage.")
    
    if pl.hp <= 0:
        addText("You died!")
        pl.hp = 0
        game = False
    
def attackEnemy(num):
    global game
    addText("Dealt "+str(enPos[num].attacked(pl.knowledge,1))+" damage to "+enPos[num].name)     
    if pl.sugar > 0:
        addText("You feel a little woozy...")
        pl.knowledge = pl.knowledge/(2*(2**(pl.sugar-1)))
        pl.sugar = 0

    if enPos[num].hp <= 0:
        pl.giveXP(enPos[num].xp)
        updateStats()
        addText(enPos[num].name+" died!")
        canvas.delete(en[num])
        board[enPos[num][0]][enPos[num][1]] = 0
        if enPos[num].name == "Rick Perry":
            game = False
        del enPos[num]
        del en[num]
  
def stuffHappens(jeff):
    global pos
    global enPos
    oldPos = [pos[0]-jeff[0], pos[1]-jeff[1]]
    
    if c[0] == 1 and c[1] == 1 and pos == [12,0] and pl.inv[2] <= 0:
        addText("That door is locked, dingus")
        pos = oldPos 
    elif pos[0] <= 0:
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
    elif board[pos[0]][pos[1]] >= 2: #when player attacks an enemy
        attackEnemy(board[pos[0]][pos[1]] - 2) #Replace with a lower stats thing
        pos = oldPos
    drawPlayer()
    
    if len(enPos) > 0 and enPos[0].name == "Rick Perry":
        cen = [enPos[0][0]+1, enPos[0][1]+1]
        dx = cen[0] - pos[0]
        dy = cen[1] - pos[1]
        newX = cen[0]
        newY = cen[1]
        if math.fabs(dx) > math.fabs(dy):
            newX = cen[0] - int(dx/math.fabs(dx))
        elif math.fabs(dy) > math.fabs(dx):
            newY = cen[1] - int(dy/math.fabs(dy))
        elif randint(0,1) == 0:
            newX = cen[0] - int(dx/math.fabs(dx))
        else:
            newY = cen[1] - int(dy/math.fabs(dy))
            
        if newX-1 <= 0 or newX+1 >= 25 or newY-1 <= 0 or newY+1 >= 25:
            newX = cen[0]
            newY = cen[1]
        elif math.fabs(newX-pos[0]) <= 1 and math.fabs(newY-pos[1]) <= 1:
            newX = cen[0]
            newY = cen[1]
            attackPlayer(0)
        
        for i in range(0,3):
            for j in range(0,3):
                board[enPos[0][0]+i][enPos[0][1]+j] = 0
                board[newX-1+i][newY-1+j] = 2
        
        enPos[0].updatePos(newX-1,newY-1)
        drawEnemy(enPos[0][0], enPos[0][1], 65)    
        
    else:
        for i in range(0,len(enPos)):
            dx = enPos[i][0] - pos[0]
            dy = enPos[i][1] - pos[1]
            newX = enPos[i][0]
            newY = enPos[i][1]
            if math.fabs(dx) > math.fabs(dy):
                newX = enPos[i][0] - int(dx/math.fabs(dx))
            elif math.fabs(dy) > math.fabs(dx):
                newY = enPos[i][1] - int(dy/math.fabs(dy))
            elif randint(0,1) == 0:
                newX = enPos[i][0] - int(dx/math.fabs(dx))
            else:
                newY = enPos[i][1] - int(dy/math.fabs(dy))
                
            if math.fabs(board[newX][newY]) >= 2 or newX <= 0 or newX >= 24 or newY >= 24 or newY <= 0:
                newX = enPos[i][0]
                newY = enPos[i][1]
            elif newX == pos[0] and newY == pos[1]:
                attackPlayer(i)
                newX = enPos[i][0]
                newY = enPos[i][1]
                
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
    updateStats()
    if not game:
        endGame()   
    
def addText(txt):
    if c[2] == 480:
        text.delete("all")
        c[2] = 0
    else:
        c[2] += 20
    text.create_text(2,c[2],text=txt,anchor='nw',font=('Courier',10))

def updateStats():
    statBar.delete("all")
    
    statBar.create_text(0,0,text=" Player Stats"+
    "\n Level: "+str(pl.level)+
    "\n HP: "+str(pl.hp) + "/" +str(pl.maxhp)+
    "\n Knowledge (Attack): "+str(pl.knowledge)+  
    "\n Immunity (Defense): "+str(pl.immune)+
    "\n XP: "+str(pl.xp)+"/"+str(10*pl.level**2),
    anchor='nw',font=('Courier',10))

def left():
    if (pos[0] <= 1 and board[0][pos[1]] == 0) or (pos[1] == 0 or pos[1] == 24):
        addText("You have now reached peak neoliberalism.")
    else:
        pos[0] -= 1
    stuffHappens([-1,0])
    
def right():
    if (pos[0] >= 23 and board[24][pos[1]] == 0) or (pos[1] == 0 or pos[1] == 24):
        addText("Is this the right way?")
    else:
        pos[0] += 1
    stuffHappens([1,0])
    
def up():
    if (pos[1] <= 1 and board[pos[0]][0] == 0) or (pos[0] == 0 or pos[0] == 24):
        addText("Y'all are just so uppity!")
    else:
        pos[1] -= 1
    stuffHappens([0,-1])
    
def down():
    if (pos[1] >= 23 and board[pos[0]][24] == 0) or (pos[0] == 0 or pos[0] == 24):
        addText("Dude, I LOVE walls!!!")
    else:
        pos[1] += 1
    stuffHappens([0,1])
    
def hi(key):
    up()
    
def hi2(key):
    down()
    
def hi3(key):
    left()
    
def hi4(key):
    right()
    
def interact():
    if board[pos[0]][pos[1]] == -1:
        q = randint(0,10)
        if q == 0:
            pl.inv[2] += 1
            addText("You gained a key. Door unlocked!")
            updateStats()
        elif q == 1:
            pl.inv[3] += 1
            addText("You have gained a lamp. Let there be light")
            updateStats()
        elif q == 2 or q == 3:
            pl.inv[1] += 1
            addText("You got some C6H1206 (glucose). Sweet!")
        elif q >=4 and q<=7:
            r = randint(1,3)
            pl.inv[0] += r
            if r == 1:
                addText("You have gained 1 health potion.")
            else:
                addText("You have gained " + str(r) + " health potions.")
        else:
            addText("This box has nothing, because we're mean")
        board[pos[0]][pos[1]] = -65
    elif board[pos[0]][pos[1]] == -65:
        addText("Again? Seriously?")
    else:
        addText("Nothing to see here...")
    updateStats()
        
def potion():
    if pl.inv[0] > 0:
        pl.inv[0] = pl.inv[0] -1;
        addText("A awfully tacky red potion. You drink it.")
        pl.hp = min(pl.hp+5,pl.maxhp)
        updateStats()
    else:
        addText("No soup for you!")
    updateStats()

def sugar():
    pl.inv[1] = pl.inv[1]-1
    if pl.inv[1] < 0:
        addText( "No more Skittles for you.")
        pl.inv[1] = 0
    else:
        addText("An oncoming sugar rush has increased your next attack!")
        pl.sugar +=1
        pl.knowledge = pl.knowledge*2
    updateStats()

def backpack():
    statBar.delete("all")
    item = ""
    if pl.inv[2]>=1 or pl.inv[3]>=1:
        item += " Key Items:\n"    
        if pl.inv[2] >= 1:
            item += " Mysterious Key\n"
        if pl.inv[3] >= 1:
            item += " Oil Lamp\n"
    if pl.inv[0] >= 1 or pl.inv[1]>=1:
        item += "\n Consumables:\n"
        if pl.inv[0] >= 1:
            item += " Health Potion (x" + str(pl.inv[0]) + ")\n"
        if pl.inv[1] >= 1:
            item += " Sugar (x" + str(pl.inv[1]) + ")\n"
    statBar.create_text(0,0,text=
    "Backpack \n\n" + str(item),
    anchor='nw',font=('Courier',10))

frame = tk.Frame(root)
root.bind("<Up>", hi)
root.bind("<Down>", hi2)
root.bind("<Left>", hi3)
root.bind("<Right>", hi4)
tk.Button(frame, text="Left", command=left).grid(row=1, column=0, columnspan=2)
tk.Button(frame, text="Right", command=right).grid(row=1, column=2, columnspan=2)
tk.Button(frame, text="Up", command=up).grid(row=0, column=1, columnspan=2)
tk.Button(frame, text="Down", command=down).grid(row=2, column=1, columnspan=2)
tk.Button(frame, text="Interact", command=interact).grid(row=0, column=5)
tk.Button(frame, text="Health Potion", command = potion).grid(row=1, column=5)
tk.Button(frame, text="Eat Sugar", command = sugar).grid(row=1, column=6)
tk.Button(frame, text="Backpack", command = backpack).grid(row=0, column=6)

frame.grid(row=1,column=0, columnspan=1)
updateStats()
    
root.mainloop()
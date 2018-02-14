import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.grid(row=0, column=0)
text = tk.Canvas(root, height=500, width=500, bg="white")
text.grid(row=0, column=1)
pos = [randint(1,23), randint(1,23)]
player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
board = []
rooms = [[[-1], [False,False,True,False], [-1]],[[False,False,True,True], [True,True,True,True], [False,True,True,False]],[[True,False,False,True], [True,True,True,True], [True,True,False,False]],[[-1],[True,False,False,False],[-1]]]
c = [3,1,-20]

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
     
def drawPlayer():
    global player
    canvas.delete(player)
    player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
    
drawPlayer()

def newRoom():
    global doors
    global rooms
    q = 0
    temp = [0,0]
    for door in doors:
        canvas.delete(door)
    for i in range(0,4):
        jeff = [[12,0,12,24],[0,12,24,12]]
        z = i
        if i>=2:
            q = 480
            z = i-2
            temp = [480,480,480,480]
        if rooms[c[0]][c[1]][i]:
            temp[z] = 240
            doors.append(canvas.create_rectangle(temp[0], temp[1], temp[0]+20, temp[1]+20, fill="blue"))
            temp[z] = q
            board[jeff[0][i]][jeff[1][i]] = 1
        else:
            board[jeff[0][i]][jeff[1][i]] = 0
                
def stuffHappens():
    if board[pos[0]][pos[1]] == 1:
        if pos[0] == 0:
            c[1] -= 1
            newRoom()
            pos[0] = 24
        elif pos[0] == 24:
            c[1] += 1
            newRoom()
            pos[0] = 0
        elif pos[1] == 0:
            c[0] -= 1
            newRoom()
            pos[1] = 24
        elif pos[1] == 24:
            c[0] += 1
            newRoom()
            pos[1] = 0
    drawPlayer()
    
def addText(txt):
    if c[2] == 480:
        text.delete("all")
        c[2] = 0
    else:
        c[2] += 20
    text.create_text(2,c[2],text=txt,anchor='nw',font=('Courier'))

def left():
    if (pos[0] <= 1 and board[0][pos[1]] == 0) or (pos[1] == 0 or pos[1] == 24):
        addText("You have now reached peak neoliberalism.")
    else:
        pos[0] -= 1
    stuffHappens()
    
def right():
    if (pos[0] >= 23 and board[24][pos[1]] == 0) or (pos[1] == 0 or pos[1] == 24):
        addText("Is this the right way?")
    else:
        pos[0] += 1
    stuffHappens()
    
def up():
    if (pos[1] <= 1 and board[pos[0]][0] == 0) or (pos[0] == 0 or pos[0] == 24):
        addText("Y'all are just so uppity!")
    else:
        pos[1] -= 1
    stuffHappens()
    
def down():
    if (pos[1] >= 23 and board[pos[0]][24] == 0) or (pos[0] == 0 or pos[0] == 24):
        addText("Dude, I LOVE walls!!!")
    else:
        pos[1] += 1
    stuffHappens()
    
frame = tk.Frame(root)
tk.Button(frame, text="Left", command=left).grid(row=0, column=0)
tk.Button(frame, text="Right", command=right).grid(row=0, column=1)
tk.Button(frame, text="Up", command=up).grid(row=0, column=2)
tk.Button(frame, text="Down", command=down).grid(row=0, column=3)

frame.grid(row=1,column=0, columnspan=2)

root.mainloop()
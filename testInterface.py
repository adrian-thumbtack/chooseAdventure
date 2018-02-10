import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg="black")
canvas.grid()
pos = [randint(0,24), randint(0,24)]
player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="lime")
board = []
lock = True
doors = []

for i in range(0,25):
    board.append([])
    for j in range(0,25):
        board[i].append(0)

total = 0
while total<5:
    q = [randint(0,24),randint(0,24)]
    while q[0] == pos[0] and q[1] == pos[1]:
        q = [randint(0,24), randint(0,24)]
    board[q[0]][q[1]] = 1
    doors.append(canvas.create_rectangle(20*q[0], 20*q[1], 20*(q[0]+1), 20*(q[1]+1), fill="blue"))
    total += 1

while (q[0] == pos[0] and q[1] == pos[1]) or board[q[0]][q[1]] != 0:
    q = [randint(0,24), randint(0,24)]
board[q[0]][q[1]] = 2
key = canvas.create_rectangle(20*q[0], 20*q[1], 20*(q[0]+1), 20*(q[1]+1), fill="yellow")

def drawPlayer():
    global player
    canvas.delete(player)
    player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="lime")
    
def resetBoard():
    global key
    global lock
    for door in doors:
        canvas.delete(door)
    canvas.delete(key)
    for i in range(0,len(board)):
        for j in range(0, len(board[i])):
            board[i][j] = 0
    
    lock = True
    pos = [randint(0,24), randint(0,24)]
    drawPlayer()
    total = 0
    while total<5:
        q = [randint(0,24),randint(0,24)]
        while q[0] == pos[0] and q[1] == pos[1]:
            q = [randint(0,24), randint(0,24)]
        board[q[0]][q[1]] = 1
        doors.append(canvas.create_rectangle(20*q[0], 20*q[1], 20*(q[0]+1), 20*(q[1]+1), fill="blue"))
        total += 1

    while (q[0] == pos[0] and q[1] == pos[1]) or board[q[0]][q[1]] != 0:
        q = [randint(0,24), randint(0,24)]
    board[q[0]][q[1]] = 2
    key = canvas.create_rectangle(20*q[0], 20*q[1], 20*(q[0]+1), 20*(q[1]+1), fill="yellow")
    
def stuffHappens():
    global player
    global lock
    if board[pos[0]][pos[1]] == 1 and not lock:
        resetBoard()
    elif board[pos[0]][pos[1]] == 2:
        lock = False
        for door in doors:
            canvas.itemconfig(door, fill="cyan")
        drawPlayer()
    else:
        drawPlayer()
    
def leftUp(i):
    if pos[i] == 0:
        pos[i] = 24
    else:
        pos[i] -= 1
    stuffHappens()

def rightDown(i):
    if pos[i] == 24:
        pos[i] = 0
    else:
        pos[i] += 1
    stuffHappens()

def left():
    leftUp(0)
    
def right():
    rightDown(0)
    
def up():
    leftUp(1)
    
def down():
    rightDown(1)

frame = tk.Frame(root)
tk.Button(frame, text="Left", command=left).grid(row=0, column=0)
tk.Button(frame, text="Right", command=right).grid(row=0, column=1)
tk.Button(frame, text="Up", command=up).grid(row=0, column=2)
tk.Button(frame, text="Down", command=down).grid(row=0, column=3)

frame.grid()

for i in range(1, 25):
    canvas.create_line(0, 20*i, 500, 20*i, fill="white")
    canvas.create_line(20*i, 0, 20*i, 500, fill="white")

root.mainloop()

import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.grid()
pos = [randint(1,23), randint(1,23)]
player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
board = []

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
canvas.create_rectangle(240, 0, 260, 20, fill="blue")
     
def drawPlayer():
    global player
    canvas.delete(player)
    player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
    
drawPlayer()

def stuffHappens():
    global player
    #if board[pos[0]][pos[1]] == 1:
    drawPlayer()

def left():
    if pos[0] <= 1 and board[0][pos[1]] == 0:
        print "Cannot move in that direction"
    else:
        pos[0] -= 1
    stuffHappens()
    
def right():
    if pos[0] >= 23 and board[24][pos[1]] == 0:
        print "Cannot move in that direction"
    else:
        pos[0] += 1
    stuffHappens()
    
def up():
    if pos[1] <= 1 and board[pos[0]][0] == 0:
        print "Cannot move in that direction"
    else:
        pos[1] -= 1
    stuffHappens()
    
def down():
    if pos[1] >= 23 and board[pos[0]][24] == 0:
        print "Cannot move in that direction"
    else:
        pos[1] += 1
    stuffHappens()
    
def checkMove(i):
    pass
    
frame = tk.Frame(root)
tk.Button(frame, text="Left", command=left).grid(row=0, column=0)
tk.Button(frame, text="Right", command=right).grid(row=0, column=1)
tk.Button(frame, text="Up", command=up).grid(row=0, column=2)
tk.Button(frame, text="Down", command=down).grid(row=0, column=3)

frame.grid()

root.mainloop()
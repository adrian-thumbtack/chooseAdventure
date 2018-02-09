import Tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg="black")
canvas.grid()
pos = [randint(0,24), randint(0,24)]
player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")

def drawPlayer():
    global player
    player = canvas.create_oval(20*pos[0], 20*pos[1], 20*(pos[0]+1), 20*(pos[1]+1), fill="green")
    
def leftUp(i):
    global player
    if pos[i] == 0:
        pos[i] = 24
    else:
        pos[i] -= 1
    canvas.delete(player)
    drawPlayer() 

def rightDown(i):
    global player
    if pos[i] == 24:
        pos[i] = 0
    else:
        pos[i] += 1
    canvas.delete(player)
    drawPlayer()

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
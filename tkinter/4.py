from tkinter import *
from tkinter import ttk

WIDTH = 600
HEIGHT = 400

class Ball():
    def __init__(self,x,y,r):
        R = r
        cx, cy = x,y
        self.id = canvas.create_oval(cx - R, cy - R, cx + R, cy + R,fill="white", outline="black", width=2)
    def update_color(self,rgb):
        #color = "#{:06x}".format(rgb)
        canvas.itemconfig(self.id,fill='#' + rgb)



def solve():
    s = en.get().strip()
    return ''.join(f'{255 - int(s[i:i+2], 16):02X}' for i in range(0, 6, 2))

def tick():
    if len(en.get()) == 6:
        b1.update_color(en.get())
        b2.update_color(solve()) 

    root.after(50,tick)

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title("Цвета")
en = ttk.Entry()
en.pack()
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

b1 = Ball(WIDTH/3,HEIGHT/2,80)
b2 = Ball(2 * WIDTH/3,HEIGHT/2,80)
tick()
root.mainloop()




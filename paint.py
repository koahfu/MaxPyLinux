from tkinter import *
from tkinter import colorchooser
from pathlib import Path
m = Path(__file__).resolve().parent
root = Tk()
root.iconbitmap(str(m)+r'\\'+r'patrik.ico')
a = '#000000'
h = 5
x = y = None
def sdraw(event):
    global x,y
    x, y = event.x, event.y
def draw(event):
    global x,y
    c.create_oval(x-h,y-h,x+h,y+h,fill=a,outline='')
    x, y = event.x, event.y
def size():
    global h
    h = e.get()
def color():
    global a
    a = colorchooser.askcolor()[1]
    if a is not None:
        a = a
    else:
        a = "#000000"
c = Canvas(height=300,width=400)
e = Entry()
x = Button(text='Set color', command=color)
b = Button(text='Set size', command=size)
c.pack(pady=5)
e.pack(pady=20)
b.pack(pady=10)
x.pack(pady=5)
c.bind('<Button-1>', sdraw)
c.bind('<B1-Motion>', draw)
root.mainloop()
from colorama import init
from tkinter import *
init()
from os import system
from pathlib import Path
from colorsys import hsv_to_rgb
class Helpful:
    pathoffile = Path(__file__)
    def pause():
        system('pause')
    def clearterminal():
        system('cls')
    newline = '\n'
class UI:
    def x():
        return Tk()
    def xsize(tk, size):
        tk.geometry(size)
    def Label(x,Text,font):
        return Label(x,text=Text,font=font)
    def pack(tkui):
        tkui.pack()
    def Image(x,path):
        return Label(x,image=path)
    def Button(x,text, cmd):
        return Button(x,text=text,command=cmd)
    def ImageButton(x,text,cmd,image):
        return Button(x,text=text,command=cmd, image=image)
    def xpack(tk):
        tk.mainloop()
    def TextBox(x):
        return Entry(x)
    def getTB(TextBox):
        TextBox.get()
    def config(tkui, **settings):
        tkui.config(settings)
    def bindtype(num) -> str:
        """Choose from 1 to 15"""
        list_ = ['<Button-1>', '<Button-2>', '<Button-3>',
                 '<Double-Button-1>', '<Double-Button-2>', '<Double-Button-3>',
                 '<ButtonRelease-1>', '<ButtonRelease-2>', '<ButtonRelease-3>',
                 '<B1-Motion>', '<B2-Motion>', '<B3-Motion>',
                 '<Enter>','Leave','MouseWheel']
        return list_[num]
    def bind(tkui,bindtype,command):
        tkui.bind(bindtype,command)
class ColorsNText:
    def rgbtotext(r,g,b):
        return f'\033[38;2;{r};{g};{b}m'
    def rgbtobg(r,g,b):
        return f'\033[48;2;{r};{g};{b}m'
    def rgbtoall(r,g,b,rx,gx,bx):
        return f'\033[38;2;{r};{g};{b};48;2;{rx};{gx};{bx}m'
    def clear():
        return '\033[0m'
    def hsvtorgb(h,s,v):
        r, g, b = hsv_to_rgb(h/255.0,s/255.0,v/255.0)
        return [int(r*255),int(g*255),int(b*255)]
    def hextorgb(withouthashtag, hex_):
        if withouthashtag:
            hexd = hex_.lstrip('#')
        return [int(hexd[i:i+2], 16) for i in (0,2,4)]
class Math:
    def factorial(n):
        if n==0:
            return 1
        else:
            return n*Math.factorial(n-1)
    def square(n):
        return n**2
    def npowern(n):
        return n**n
class Test:
    name = 'Jackbooooks'
    type = 'module'
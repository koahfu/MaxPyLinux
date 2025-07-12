import subprocess as sg
from tkinter import *
from random import randint
root = Tk()
root.geometry('100x40')
def cmd2(event):
    sg.Popen("start cmd", shell=True)
def cmd():
    cmdb.config(text=str(randint(1,1000000000000)))
cmdb = Button(root, text='Запуск (ПКМ)', command=cmd)
cmdb.pack()
cmdb.bind('<Button-3>', cmd2)
root.mainloop()
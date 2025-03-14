import random
from tkinter import *
from tkinter import messagebox
from random import randint

def gol():
    pass

def log(event):
    btn_no.place(x = randint(20,330), y = randint(10,130))

def yes():
    messagebox.showinfo(' ',"Спасибо за ответ)")
    quit()

win = Tk()
win.geometry('350x150')
win.title("Вопрос")
win.protocol("WM_DELETE_WINDOW", gol)
win.resizable(width = False, height = False)

label = Label(text = "Сосал?", font="Arial 15").pack()

btn_yes = Button(text = "  Да  ",command=yes ,font="Arial 15")
btn_yes.place(x='60', y='50')


btn_no = Button(text = "  Нет  ", font="Arial 15")
btn_no.place(x='210', y='50')
btn_no.bind('<Enter>', log)

win.mainloop()


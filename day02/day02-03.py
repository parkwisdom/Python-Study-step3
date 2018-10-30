from tkinter import *

def clickButton():
    print('나불렀어?')

window = Tk()
window.geometry('400x400')

label1 = Button(window,text ='ㅋㅋㅋㅋ',command = clickButton)
photo = PhotoImage(file='D:/images/cat2.gif')
label2 = Label(window, image=photo)

label1.pack()
label2.pack()

window.mainloop()
##GIF 이미지 뷰어
from tkinter import *
from tkinter.filedialog import *

#함수선언부
def openFile():
    filename = askopenfilename(parent=window, filetypes=(('GIF파일', '*.gif'), ('모든파일', '*.*')))
    photo = PhotoImage(file= filename)
    pLabel.configure(image= photo)
    pLabel.image = photo

def exitFile():
    pass

def myPick():
    labelImage.configure(image =photo)
    labelImage.image = photo



#변수선언부

#메인코드부

window = Tk()
window.geometry('400x400')

#빈사진 준비
photo = PhotoImage()
pLabel = Label(window, image= photo)
pLabel.pack(expand=1,anchor= CENTER)


mainMenu =Menu(window)
window.config(menu=mainMenu)
label1 =Label(window,text ="입력된 값:")
label1.pack()
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu=fileMenu)
fileMenu.add_command(label = '열기(Ctrl+O)',command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label = '종료(Ctrl+X)',command=exitFile)

var = IntVar()
rb1 = Radiobutton(window,text="강아지", variable = var,value=1)
rb2 = Radiobutton(window,text="고양이", variable = var,value=2)
rb3 = Radiobutton(window,text="토끼", variable = var,value=3)
buttonCl=Button(window,text='사진보기',command =myPick )

photo=PhotoImage(file="d:/images/cat2.gif")

labelImage = Label(window,width=200,height=200,image=None)

rb1.pack(padx=5,pady=5)
rb2.pack(padx=5,pady=5)
rb3.pack(padx=5,pady=5)
buttonCl.pack(padx=5,pady=5)
labelImage.pack(padx=5,pady=5)

window.mainloop()
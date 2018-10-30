from tkinter import *
from tkinter.filedialog import *
import operator

def openFile():
    global photo
    filename = askopenfilename(parent = window, filetypes= (('GIF파일','*.gif'),('모든파일','*.*')))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo

def exitFile():
    window.quit()
    window.destroy()


def analyzeGIF():
    global photo
    rDic,gDic,bDic = {},{},{} #색상 개수 딕셔너리
    xSize = photo.width()
    ySize = photo.height()
    # print(xSize,ySize)
    # pass
    # for i in range(xSize):
    #     for k in range(ySize):
    #         r,g,b = photo.get(i,k)
    #         if r in rDic:
    #             rDic[r]+=1
    #         else:
    #             rDic[r]=1
    # # print(rDic)
    # countList = sorted(rDic.items(),key=operator.itemgetter(1))
    # print('최소출현 r픽셀값:',countList[0])
    # print('최다출현 r픽셀값:',countList[-1])

    for i in range(xSize):
        for k in range(ySize):
            r,g,b = photo.get(i,k)
            if r in rDic:
                rDic[r]+=1
            else:
                rDic[r]=1
            if g in gDic:
                gDic[g] += 1
            else:
                gDic[g] = 1
            if b in bDic:
                bDic[b] += 1
            else:
                bDic[b] = 1
    # print(rDic)
    rList = sorted(rDic.items(),key=operator.itemgetter(1))
    gList = sorted(gDic.items(),key=operator.itemgetter(1))
    bList = sorted(bDic.items(),key=operator.itemgetter(1))
    print('최소/최다출현 r픽셀값:',rList[0],rList[-1])
    print('최소/최다출현 g픽셀값:',gList[0],gList[-1])
    print('최소/최다출현 b픽셀값:',bList[0],bList[-1])



#전역변수
photo= None

#메인코드
window = Tk()
window.geometry('400x400')

#빈사진 준비
photo = PhotoImage()
pLabel = Label(window, image= photo)
pLabel.pack(expand=1,anchor= CENTER)


mainMenu =Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu=fileMenu)
fileMenu.add_command(label = '열기(Ctrl+O)',command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label = 'GIF데이터',command=analyzeGIF)
fileMenu.add_separator()
fileMenu.add_command(label = '종료(Ctrl+X',command=exitFile)

window.mainloop()
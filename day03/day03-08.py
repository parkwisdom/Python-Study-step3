##영상 처리 및 데이터 분석 툴
from tkinter import *
import os.path
import math

##함수 선언부
def loadImage(fname):
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
    fsize = os.path.getsize(fname) #파일 크기 확인
    inH=inW=int(math.sqrt(fsize))  #중요한 역할! 입력 메모리 크기결정. 메모리 크기를 확보하기 위해서 필요
    inImage=[]
    tmpList=[]
    for i in range(inH): #입렵 메모리 확보 (0으로 초기화)
        tmpList=[]
        for k in range(inW):
            tmpList.append(0)
        inImage.append(tmpList)
    #파일 =->메모리로 데이터 로딩
    fp=open(fname,'rb') #파일 열기 (바이너리 모드)
    for i in range(inH):
        for k in range(inW):
            inImage[i][k]=int(ord(fp.read(1)))
    fp.close()
    print(inImage[100][100])

def openFile():
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
    filename='D:/images/512.raw'
    loadImage(filename)
    pass

def saveFile():
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
    pass

def exitFile():
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
    pass

def editFile():
    pass

##전역 변수부
inImage, outImage=[],[]; inW,inH,outW,outH=[0]*4
window, canvas,paper,filename = [None]*4

##메인 코드부
window=Tk(); window.geometry('400x400')
window.title('영상 처리&데이터 분석 Ver 0.01')

mainMenu =Menu(window); window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu=fileMenu)
fileMenu.add_command(label = '열기',command=openFile)
fileMenu.add_command(label = '저장',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = '종료',command=exitFile)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '편집',menu=editMenu)
editMenu.add_command(label = '복사',command=lambda :editFile(1))
editMenu.add_command(label = '붙여넣기',command=lambda :editFile(2))
editMenu.add_command(label = '잘라내기',command=lambda :editFile(3))

window.mainloop()
##영상 처리 및 데이터 분석 툴
from tkinter import *
import os.path
import math
from tkinter.simpledialog import *
from tkinter.filedialog import *

##함수 선언부
def loadImage(fname):
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH

    photo = PhotoImage(file=filename)
    inW=photo.width(); inH=photo.height()

    inImageR, inImageG, inImageB=[],[],[]
    tmpList=[]
    for i in range(inH): #입렵 메모리 확보 (0으로 초기화)
        tmpList=[]
        for k in range(inW):
            tmpList.append(0)
        inImageR.append(tmpList[:])
        inImageG.append(tmpList[:])
        inImageB.append(tmpList[:])

    #파일 =->메모리로 데이터 로딩
    for i in range(inH):
        for k in range(inW):
            r,g,b=photo.get(i,k)
            inImageR[i][k]=r
            inImageG[i][k]=g
            inImageB[i][k]=b

    # photo=None

def openFile():
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    filename=askopenfilename(parent=window,filetypes=(('GIF파일','*.gif'),('모든파일','*.*')))
    loadImage(filename) #파일 -->입력메모리
    equal() #입력메모리 --> 출력메모리


def display():
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    #기존 캔버스 있으면 뜯어내기
    if canvas!=None:
        canvas.destroy()

    #화면 준비(고정됨)
    window.geometry(str(outH)+ 'x'+ str(outW))
    canvas=Canvas(window,width=outW, height=outH)
    paper= PhotoImage(width =outW, height=outH)
    canvas.create_image((outW/2,outH/2),image=paper,state = 'normal')

    #화면에 출력
    for i in range(outH):
        for k in range(outW):
            dataR = outImageR[i][k]
            dataG = outImageG[i][k]
            dataB = outImageB[i][k]
            paper.put('#%02x%02x%02x' %(dataR,dataG,dataB), (i,k))

    canvas.pack()



def equal(): #동일영상 알고리즘
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    #중요! 출력메모리의 크기를 결정
    outW=inW; outH=inH
    outImageR, outImageG, outImageB = [],[],[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList[:])
        outImageG.append(tmpList[:])
        outImageB.append(tmpList[:])

    #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
    for i in range(inH):
        for k in range(inW):
            outImageR[i][k]=inImageR[i][k]
            outImageG[i][k]=inImageG[i][k]
            outImageB[i][k]=inImageB[i][k]
    display()


def addImage(): #밝게하기 알고리즘
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    #중요! 출력메모리의 크기를 결정
    outW=inW; outH=inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
    value = askinteger('밝게하기','밝게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k]+value>255:
                outImage[i][k]=255
            else:
                outImage[i][k]=inImage[i][k] + value
    display()

def subImage(): #어둡게하기 알고리즘
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    #중요! 출력메모리의 크기를 결정
    outW=inW; outH=inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
    value = askinteger('어둡게하기','어둡게할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k]-value < 0:
                outImage[i][k]=0
            else:
                outImage[i][k]=inImage[i][k] - value
    display()

def multImage(): #곱하기 알고리즘
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageBe,inW,inH,outW,outH
    #중요! 출력메모리의 크기를 결정
    outW=inW; outH=inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
    value = askinteger('곱하기','곱할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k]*value > 255:
                outImage[i][k]=255
            elif inImage[i][k]*value < 0:
                outImage[i][k]=0
            else:
                outImage[i][k]=inImage[i][k] * value
    display()

def divImage(): #나눗셈하기 알고리즘
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    #중요! 출력메모리의 크기를 결정
    outW=inW; outH=inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
    value = askinteger('나눗셈하기','나누셈할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k]//value > 255:
                outImage[i][k]=255
            elif inImage[i][k] // value < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k]=inImage[i][k] // value

    display()


def negatransImage(): #반전하기 알고리즘
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    #중요! 출력메모리의 크기를 결정
    outW=inW; outH=inH
    outImage = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
    value = askinteger('반전하기','반전할 값-->',minvalue=1,maxvalue=255)
    for i in range(inH):
        for k in range(inW):
                outImage[i][k]=255-inImage[i][k]
    display()

#---------------감마 미완성

# def gammaImage(): #감마 알고리즘
#     global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
#     #중요! 출력메모리의 크기를 결정
#     outW=inW; outH=inH
#     outImage = []
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)
#     #★★★★★진짜 영상처리 알고리즘을 구현★★★★★
#     value = askinteger('감마','감마-->',minvalue=1,maxvalue=255)
#     for i in range(inH):
#         for k in range(inW):
#
#             if pow(inImage[i][k],1/value) > 255:
#                 outImage[i][k]=255
#             elif pow(inImage[i][k],1/value) < 0:
#                 outImage[i][k] = 0
#             else:
#                 outImage[i][k]=pow(inImage[i][k],1/value)
#     display()




def saveFile():
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    pass

def exitFile():
    global window, canvas,paper,filename,inImageR,inImageG,inImageB, outImageR,outImageG,outImageB,inW,inH,outW,outH
    pass

def editFile():
    pass

##전역 변수부
inImageR,inImageG,inImageB, outImageR,outImageG,outImageB=[[]]*6; inW,inH,outW,outH=[0]*4
window, canvas,paper,filename = [None]*4

##메인 코드부
window=Tk(); window.geometry('400x400')
window.title('영상 처리&데이터 분석 Ver 0.02')

mainMenu =Menu(window); window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu=fileMenu)
fileMenu.add_command(label = '열기',command=openFile)
fileMenu.add_command(label = '저장',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = '종료',command=exitFile)

pixelMenu = Menu(mainMenu) ; mainMenu.add_cascade(label='화소점처리',menu=pixelMenu)
pixelMenu.add_command(label='동일영상',command=equal)
pixelMenu.add_command(label='밝게하기',command=addImage)
pixelMenu.add_command(label='어둡게하기',command=subImage)
pixelMenu.add_command(label='곱하기',command=multImage)
pixelMenu.add_command(label='나눗셉하기',command=divImage)
pixelMenu.add_command(label='반전하기',command=negatransImage)
# pixelMenu.add_command(label='감마값구하기',command=gammaImage)




# editMenu = Menu(mainMenu)
# mainMenu.add_cascade(label = '편집',menu=editMenu)
# editMenu.add_command(label = '복사',command=lambda :editFile(1))
# editMenu.add_command(label = '붙여넣기',command=lambda :editFile(2))
# editMenu.add_command(label = '잘라내기',command=lambda :editFile(3))

window.mainloop()
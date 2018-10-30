##영상 처리 및 데이터 분석 툴
from tkinter import *
import os.path
import math
from tkinter.simpledialog import *
from tkinter.filedialog import *
import operator

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
    # print(inImage[100][100])

def openFile():
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
    filename='D:/images/128.raw'
    loadImage(filename) #파일 -->입력메모리
    equal() #입력메모리 --> 출력메모리


def display():
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
            data = outImage[i][k]
            paper.put('#%02x%02x%02x' %(data,data,data), (k,i))
    canvas.pack()



def equal(): #동일영상 알고리즘
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    for i in range(inH):
        for k in range(inW):
            outImage[i][k]=inImage[i][k]
    display()

def addImage(): #밝게하기 알고리즘
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
#     global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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

def a_average(): #입출력 영상의 평균값
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
    rawSum=0
    for i in range(inH):
        for k in range(inW):
            rawSum+= inImage[i][k]
    inRawAvg = int(rawSum/(inH*inW))

    rowSum=0
    for i in range(outH):
        for k in range(outW):
            rawSum += outImage[i][k]
    outRawAvg = int(rawSum/(outH*outW))

    subWindow = Toplevel(window) #부모window에 종속된 서브윈도
    subWindow.geometry('200x100')
    label1=Label(subWindow, text= '입력영상 평균값-->' + str(inRawAvg)); label1.pack()
    label2=Label(subWindow, text= '출력영상 평균값-->' + str(outRawAvg)); label2.pack()
    subWindow.mainloop()


def a_size(): #입출력 영상의 최댓값/최솟값
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH

    rawSizeDic={}
    for i in range(inH):
        for k in range(inW):
            rawSize = inImage[i][k]
            if rawSize in rawSizeDic:
                rawSizeDic[rawSize]+=1
            else:
                rawSizeDic[rawSize]=1
    inSizeList = sorted(rawSizeDic.items(),key=operator.itemgetter(1))

    rawSizeDic={}
    for i in range(outH):
        for k in range(outW):
            rawSize = outImage[i][k]
            if rawSize in rawSizeDic:
                rawSizeDic[rawSize]+=1
            else:
                rawSizeDic[rawSize]=1
    outSizeList = sorted(rawSizeDic.items(),key=operator.itemgetter(1))

    subWindow = Toplevel(window) #부모window에 종속된 서브윈도
    subWindow.geometry('300x100')
    label3=Label(subWindow, text= '입력 영상 최대/최소값-->' + str(inSizeList[-1]) + str(inSizeList[0])) ; label3.pack()
    label4=Label(subWindow, text= '출력 영상 최대/최소값-->' + str(outSizeList[-1]) + str(outSizeList[0])) ; label4.pack()
    subWindow.mainloop()


def upDown(): #상하반전 알고리즘
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    for i in range(inH):
        for k in range(inW):
            outImage[outW-1-i][k]=inImage[i][k]
    display()

def rightLeft(): #좌우반전 알고리즘
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH
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
    for i in range(inH):
        for k in range(inW):
            outImage[i][outH-1-k]=inImage[i][k]
    display()

def panImage():
    global panYN
    panYN = True

def mouseClick(event):
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH,sx,sy,ex,ey,panYN
    if not panYN:
        return
    sx=event.x; sy=event.y;

def mouseDrop(event):
    global window, canvas,paper,filename,inImage, outImage,inW,inH,outW,outH,sx,sy,ex,ey,panYN
    if not panYN:
        return
    ex=event.x; ey=event.y;
    mx=sx-ex; my=sy-ey

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
    for i in range(inH):
        for k in range(inW):
            if 0 <= i-my < outH and 0 <= k-mx < outW:
                outImage[i-my][k-mx]=inImage[i][k]
    panYN=False
    display()


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
panYN=False; sx,sy,ex,ey=[0]*4


##메인 코드부
window=Tk(); window.geometry('200x200')
window.title('영상 처리&데이터 분석 Ver 0.08')
window.bind("<Button-1>",mouseClick)
window.bind("<ButtonRelease-1>",mouseDrop)

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
pixelMenu.add_command(label='색반전하기',command=negatransImage)
# pixelMenu.add_command(label='감마값구하기',command=gammaImage)

analyzMenu=Menu(mainMenu); mainMenu.add_cascade(label='데이터분석',menu=analyzMenu)
analyzMenu.add_command(label='평균값',command=a_average)
analyzMenu.add_command(label='최댓값&최솟값',command=a_size)

geoMenu=Menu(mainMenu); mainMenu.add_cascade(label='기하학처리',menu=geoMenu)
geoMenu.add_command(label='상하반전',command=upDown)
geoMenu.add_command(label='좌우반전',command=rightLeft)
geoMenu.add_command(label='화면이동',command=panImage)


window.mainloop()
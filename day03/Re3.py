## 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리) ##

# 복습퀴즈1.GIF
# 영상데이터분석
#
# [파일] - [열기]에서 GIF영상을 선택한 후에 다음의 내용이 윈도창의 Label에 출력되도록 한다.
#
# 최소 / 최다 출현 r픽셀값: (138, 1)(189, 1612)
# 최소 / 최다 출현 g픽셀값: (137, 1)(209, 1298)
# 최소 / 최다 출현 b픽셀값: (10, 1)(99, 2531)
# r, g, b픽셀 평균값: 194.80955 159.2699 109.461
# r, g, b픽셀 중위수: 196 157 91

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
    for i in range(xSize):
        for k in range(ySize):
            r,g,b = photo.get(i,k)
            if r in rDic:
                rDic[r]+=1
            else:
                rDic[r]=1
    # print(rDic)
    # countList = sorted(rDic.items(),key=operator.itemgetter(1))
    # print('최소출현 r픽셀값:',countList[0])
    # print('최다출현 r픽셀값:',countList[-1])

    for i in range(xSize):
        for k in range(ySize):
            r,g,b = photo.get(i,k)
            if r in rDic:
                rDic[r]+=1
            else:
                gDic[g]=1
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

    rSum = 0
    for item in rList:
        rSum +=item[0]*item[1]
    rAvg = rSum/(xSize*ySize)

    gSum = 0
    for item in gList:
        gSum +=item[0]*item[1]
    gAvg = gSum/(xSize*ySize)

    bSum = 0
    for item in bList:
        bSum +=item[0]*item[1]
    bAvg = bSum/(xSize*ySize)
    print('r,g,b 픽셀 평균값:',rAvg,gAvg,bAvg)

    rList= sorted(rDic.items(),key=operator.itemgetter(0))
    gList= sorted(gDic.items(),key=operator.itemgetter(0))
    bList= sorted(bDic.items(),key=operator.itemgetter(0))
    rStream, gStream, bStream =[],[],[]

    for item in rList:
        for i in range(item[1]):
            rStream.append(item[0])
    for item in gList:
        for i in range(item[1]):
            gStream.append(item[0])
    for item in bList:
        for i in range(item[1]):
            bStream.append(item[0])

    midPos = int((xSize*ySize)/2)
    print('r,g,b픽셀 중위수: ',rStream[midPos],gStream[midPos],bStream[midPos])

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
#
# 복습퀴즈2. --> 이 문제는 제출 하지 말것 자신이 나온 사진 3장을 준비해서 각각
# 512x512, 256x256, 128x128, 64x64로 GIF, JPG(또는PNG), RAW 파일을 만든다.(PaintShop사용): 총36장파일
# (파일명은 woo512.gif, woo512.jpg, woo512.raw  등의 형식을 사용 권장.)
#
# 복습퀴즈3(선택).p325.그림판 만들기

# from tkinter import *
# from tkinter.colorchooser import *
# from tkinter.simpledialog import *
#
# #함수
# def mouseClick():
#     global x1,y1,x2,y2,penColor ,penWidth
#
#     pass
# def mouseDrop():
#     global x1,y1,x2,y2,penColor ,penWidth
#
#     pass
#
#
#
# #전역변수
# window=None
# canvas = None
# x1,y1,x2,y2=[None]*4
# penColor = 'black'
# penWidth = 5
#
# #메인코드
#
# window=Tk()
# window.title('그림판')
# canvas=Canvas(window,height = 300,width=300)
# canvas.bind("<Button-1>",mouseClick)
# canvas.bind("<Buttonlease-1>",mouseDrop)
# canvas.pack()
#




# 제목: [빅데이터]
# 복습퀴즈
# 10 / 02, 홍 * 동
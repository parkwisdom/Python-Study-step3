## 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리) ##

# 복습퀴즈1. 800x800 화면에서 거북이가 다음 정보를 소유하도록 한다.
#  [거북이개체, (시작x,y), (끝x,y), (r,g,b), 크기]
#      20마리를 생성해서 리스트에 저장한 후에, 각각 이동하도록 한다.
# import turtle
# import random
# #전역변수
# myTurtle , tX,tY,tColor,tSize, tShape = [None]*6
# shapeList=[] #거북이 모양 리스트
# playerTurtles = [] #거북이 100마리 2차원 리스트
# swidth, sheight = 800,800
#
# #메인코드
# turtle.setup(width = swidth+30,height= sheight+30)
# turtle.screensize(swidth,sheight)
# shapeList = turtle.getshapes()
# for i in range(20):
#     random.shuffle(shapeList)
#     myTurtle= turtle.Turtle(shapeList[0])
#     tX=random.randrange(-swidth/2,swidth/2)
#     tY=random.randrange(-sheight/2,sheight/2)
#     r=random.random();    g=random.random();    b=random.random();
#     tSize=random.randint(1,3)
#     playerTurtles.append([myTurtle, tX,tY,tSize,r,g,b])
#
# for tList in playerTurtles:
#     myTurtle=tList[0]
#     myTurtle.color((tList[4],tList[5],tList[6]))
#     myTurtle.pencolor((tList[4],tList[5],tList[6]))
#     myTurtle.turtlesize(tList[3])
#     myTurtle.goto(tList[1],tList[2])

# 복습퀴즈2. 구구단을 처리하되, 각 결과의 앞자리~뒷자리까지 합계로 출력한다.
#    예)  2x1=3   (값2를 02로 취급해서 0부터 2까지의 합계 : 0+1+2 = 3)
#          2x2=10 (값2를 02로 취급해서 0부터 2까지의 합계 : 0+1+2+3+4 = 10)
#          ...
#          2x9=36  (값18을 1부터 8까지 : 1+2+3+4+5+6+7+8=36)
#          ...
#          8x8=15  (값64를 6부터 4까지 : 6+5+4 = 15)
#
# sw=False
# for i in range(2,10):
#     for k in range(1,10):
#         print(i, 'x', k, '=', i * k)
#
#         a=i*k
#         a='%02d' % a
#         # print(a)
#         a=list(map(int,list(str(a))))
#         print(a)
#         for j in a:#...............?...
#             j+=a
#             print(j)
#     print('\n')



# 복습퀴즈3(심화). 행과 열의 크기를 입력받고, 크기만큼 가로 및 세로로 지그재그로
#    1부터 출력한다.
#     예) 3, 4를 입력하면
#          1   2  3   4
#          8   7  6   5
#          9 10 11 12
#
#          1   6  7  12
#          2   5  8  11
#          3   4  9  10

ROW = int(input("행-->"))
COL = int(input("열-->"))

myList=[]
tmpList=[]
for i in range(ROW):
    tmpList=[]

    for k in range(COL):
        k+=COL*i+1
        tmpList.append(k)
    myList.append(tmpList)
for i in range(ROW) :
    for k in range(COL) :
        print("%2d " % myList[i][k] , end='')
    print()

# print(myList)
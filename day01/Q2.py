import turtle
#변수 선언
num1,num2 = 0,0; swidth,sheight =1000,300; curX,curY = 0,0

#메인 코드
turtle.shape('turtle')
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)
turtle.penup(); turtle.left(90)

num1 = int(input("숫자1 -->"))
num2 = int(input("숫자2 -->"))
num3= num1&num2
binary1 = bin(num1)
binary2 = bin(num2)
res = bin(num3)
print(binary1,binary2,res)

curX = swidth / 2
curY = 100
for i in range(len(binary1)-2):

    turtle.goto(curX,curY)
    if num1 & 1:
        turtle.color('red')
        turtle.turtlesize(2)
    else:
        turtle.color('blue')
        turtle.turtlesize(1)
    turtle.stamp()
    curX-=50
    num1>>=1


curX = swidth / 2
curY = 50
for i in range(len(binary2)-2):

    turtle.goto(curX,curY)
    if num2 & 1:
        turtle.color('red')
        turtle.turtlesize(2)
    else:
        turtle.color('blue')
        turtle.turtlesize(1)
    turtle.stamp()
    curX-=50
    num2>>=1

curX = swidth / 2
curY = 0
for i in range(len(res)-2):

    turtle.goto(curX,curY)
    if num3 & 1:
        turtle.color('red')
        turtle.turtlesize(2)
    else:
        turtle.color('blue')
        turtle.turtlesize(1)
    turtle.stamp()
    curX-=50
    num3 >>=1

turtle.done()
#거북이 복습하기
import turtle
import random

# 함수 선언
def clickLeft(x,y): #파라미터, 클릭한 위치
    # print('나 불렀어?')
    r=random.random() #0~0.9999999999
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))

    turtle.pensize()
    turtle.goto(x,y)

def clickRight(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def clickMid(x,y):
    r = random.random()  # 0~0.9999999999
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    turtle.goto(x, y)

# 변수 선언
penSize =0 ; r,g,b =[0]*3
# 메인 코드
if __name__=='__main__':
    turtle.title('거북이가 그리기')
    turtle.shape('turtle')
    turtle.onscreenclick(clickLeft,1)
    turtle.onscreenclick(clickRight,3)
    turtle.onscreenclick(clickMid,2)
    turtle.done()
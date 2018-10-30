import turtle
import random

# 함수 선언

def clickMid(x,y):
    pSize = random.randrange(1, 10)
    turtle.pensize(pSize)

    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.color((r, g, b))
    turtle.goto(x, y)

# 변수 선언
r,g,b =[0]*3
# 메인 코드
if __name__=='__main__':
    turtle.title('거북이가 그리기')
    turtle.shape('turtle')
    turtle.onscreenclick(clickMid,2)
    turtle.done()
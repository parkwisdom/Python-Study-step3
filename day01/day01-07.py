#2차원 리스트 조작(완전 중요)
#3x4크기의 빈리스트 만들기

# myList =[
#     [0,0,0,0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]
ROW = int(input("행-->"))
COl = int(input("열-->"))

myList=[]
tmpList=[]
for i in range(ROW):
    tmpList=[]
    for k in range(COl):
        tmpList.append(0)
    myList.append(tmpList)
print(myList)


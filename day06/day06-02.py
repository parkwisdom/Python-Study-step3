#엑셀의 시트처럼 보이는 것 만들기

from tkinter import *

csvList=[['제목1','제목2','제목3'],
         [111,222,333],
         [444,555,666],
         [777,888,999]]


window = Tk()
# window.geometry('400x400')
rowNum = len(csvList)
colNum = len(csvList[0])
cellList = []

# ent1=Entry(window,text='0000')
# # ent1.place(x=0,y=0)
# ent1.grid(row=0,column=0)
## ent2=Entry(window,text='0000')
# # ent2.place(x=0,y=100)
# ent2.grid(row=0,column=1)

#빈시트 만들기
for i in range(0,rowNum):
    tmpList=[]
    for k in range(0,colNum):
        ent = Entry(window,text='')

        ent.grid(row=i,column=k)
        tmpList.append(ent)

    cellList.append(tmpList)

#시트에 리스트값 채우기
for i in range(0,rowNum):
    for k in range(0,colNum):
        cellList[i][k].insert(0,csvList[i][k])





window.mainloop()
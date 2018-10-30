#!/usr/bin/env  python3
import  sys  # 명령창과 연결하는 기능
from tkinter import *

window = Tk()
# 명령창 :  python  Day06-01.py  파라미터1  파라미터2 ....
input_file = "d:\\pydata\\csv\\supplier_data.csv"
output_file = "d:\\pydata\\output\\result04.csv"

filereader = open(input_file, 'r', newline='')
filewriter = open(output_file, 'w', newline='')

header = filereader.readline()
header  = header.strip() # 앞뒤 공백제거
header_list = header.split(',')
# 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.
header_str = ','.join(map(str, header_list))
filewriter.write(header_str + '\n')
for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.
    row = row.strip()
    row_list = row.split(',')
    # park Number,purchase Date
    idx1 = 0
    for h in header_list:
        if h.strip().upper()=='part Number'.strip().upper():
            break
        idx1+=1
    idx2 = 0
    for h in header_list:
        if h.strip().upper() == 'part Number'.strip().upper():
            break
        idx2 += 1
    if idx1>idx2:
        idx1,idx2=idx2,idx1

    #퀴즈 2. 값을 모두 100달라 인상
    cost = float(row_list[3][1:])
    cost+=100
    cost_str="${0:.2f}".format(cost)
    row_list[3]=cost_str

    #퀴즈 3.
    del(row_list[4])
    del(row_list[2])
    if row_list[0]=='Supplier Y':
        continue

    cost = float(row_list[2][1:])
    cost *= 1.5
    cost=int(cost/100)*100
    cost_str = "${0:.2f}".format(cost)
    row_list[2] = cost_str
    row_str = ','.join(map(str, row_list))
    # print(row_list)
    filewriter.write(row_str + '\n')


    #row_list를 [[],[],[]]이렇게 만들고 싶다./
    cell=[]
    for i in row_list:
        cell.append(row_list)
        print(cell)


    rowNum = len(row_list)
    colNum = len(row_list)
    cellList = []
    # 빈시트 만들기
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='')

            ent.grid(row=i, column=k)
            tmpList.append(ent)

        cellList.append(tmpList)

    # 시트에 리스트값 채우기
    for i in range(0, rowNum):
        for k in range(0, colNum):
            cellList[k][i].insert(0,row_list[k][i])


filereader.close()
filewriter.close()

window.mainloop()
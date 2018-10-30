#메뉴 관리
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *

def drawSheet(cList):
    rowNum = len(cList)
    colNum = len(cList[0])
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
            cellList[i][k].insert(0, cList[i][k])


def openCSV():
    global csvList
    csvList=[]
    input_file = askopenfilename(parent=window, filetypes=(('CSV파일', '*.csv'), ('모든파일', '*.*')))
    filereader = open(input_file,'r',newline='')
    header=filereader.readline()
    header = header.strip()
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)

    drawSheet(csvList)
    filereader.close()

def saveCSV():
    global csvList
    if csvList==[]:
        return
    saveFp=asksaveasfile(parent=window,mode='w',defaultextension='.csv',filetypes=(('CSV파일', '*.csv'), ('모든파일', '*.*')))
    # print(saveFp.name)
    filewriter=open(saveFp.name, 'w',newline='')
    for row_list in csvList:
        row_str=','.join(map(str,row_list))
        filewriter.writelines(row_str+'\n')

    filewriter.close()

#전역변수
csvList=[]


#메인코드
window= Tk()

mainMenu =Menu(window)
window.config(menu=mainMenu)


fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu=fileMenu)
fileMenu.add_command(label = 'CSV 열기',command=openCSV)
fileMenu.add_command(label = 'CSV 저장',command=saveCSV)


window.mainloop()
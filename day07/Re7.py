# (1) 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리)
# (2) 텍스트마이닝 기반 데이터 분석 (부제: 텍스트 기반 데이터 분석 및 처리)
# (3) 빅데이터 분석 결과 시각화 (부제 : 데이터베이스 기반 데이터 분석 및 GUI 시각화)
#
# 복습퀴즈1. 엑셀파일을 읽어서 마지막 시트를 화면에 출력한다.
#
# 복습퀴즈2. 엑셀파일을 읽어서 모든 시트를 화면에 출력한다. 단,
#       제목행은 제일 위에 한번만 출력한다.
#
# 복습퀴즈3(선택) 폴더를 선택한 후, 그 폴더의 모든 엑셀파일을 목록으로 보여준다.
#    그리고 선택한 엑셀파일의 모든 시트 목록을 보여준다. 마지막을 선택한
#    시트를 화면에 출력한다.
#



from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import csv
import json
import os
import os.path
import xlrd
import xlwt


def drawSheet(cList):
    global cellList
    print(cellList)
    if cellList == None or cellList == []:
        print('1111')
        pass
    else:
        print('2222')
        for row in cellList:
            for col in row:
                col.destroy()

    rowNum = len(cList)
    colNum = len(cList[0])
    cellList = []
    # 빈 시트 만들기
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='')
            tmpList.append(ent)
            ent.grid(row=i, column=k)
        cellList.append(tmpList)
    # 시트에 리스트값 채우기. (= 각 엔트리에 값 넣기)
    for i in range(0, rowNum):
        for k in range(0, colNum):
            cellList[i][k].insert(0, cList[i][k])




def excelData01():
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                                 filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    for worksheet in workbook.sheets():
        sheetName = worksheet.name
        sRow = worksheet.nrows
        sCol = worksheet.ncols
        print(sheetName, sRow, sCol)


def excelData02(): #복습퀴즈 1번
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                                 filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    sheet1 = workbook.sheets()[-1]
    sheetName = sheet1.name
    sRow = sheet1.nrows
    sCol = sheet1.ncols
    # print(sheetName, sRow, sCol)
    # Worksheet --> csvList
    for i in range(sRow):
        tmpList = []
        for k in range(sCol):
            value = sheet1.cell_value(i, k)
            tmpList.append(value)
        csvList.append(tmpList)

    drawSheet(csvList)


def excelData03(): #복습퀴즈 2번
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                                 filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    for worksheet in workbook.sheets():
        sRow = worksheet.nrows
        sCol = worksheet.ncols
        # Worksheet --> csvList
        for i in range(sRow):
            tmpList = []
            for k in range(sCol):
                value = worksheet.cell_value(i, k)
                tmpList.append(value)
            csvList.append(tmpList)

    drawSheet(csvList)


def excelData05(): #복습퀴즈 3번
    global csvList, input_file
    csvList = []
    input_file = askopenfilename(parent=window,
                                 filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetNameList = []
    for worksheet in workbook.sheets():
        sheetNameList.append(worksheet.name)

    ##################################
    def selectSheet():
        selectedIndex = listbox.curselection()[0]
        subWindow.destroy()
        sheet1 = workbook.sheets()[selectedIndex]
        sRow = sheet1.nrows
        sCol = sheet1.ncols
        for i in range(sRow):
            tmpList = []
            for k in range(sCol):
                value = sheet1.cell_value(i, k)
                tmpList.append(value)
            csvList.append(tmpList)
        drawSheet(csvList)

    subWindow = Toplevel(window)  # window의 하위로 지정
    listbox = Listbox(subWindow)
    button = Button(subWindow, text='선택', command=selectSheet)
    listbox.pack();
    button.pack()
    for sName in sheetNameList:
        listbox.insert(END, sName)
    subWindow.lift()

    ####################################



def saveExcel():
    global csvList, input_file
    if csvList == []:
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.xls',
                           filetypes=(("Excel파일", "*.xls"), ("모든파일", "*.*")))
    fileName = saveFp.name

    outWorkbook = xlwt.Workbook()
    outSheet = outWorkbook.add_sheet('sheet1')  # 이름을 추후에 지정하세요.

    for i in range(len(csvList)):
        for k in range(len(csvList[i])):
            outSheet.write(i, k, csvList[i][k])

    outWorkbook.save(fileName)


## 전역 변수 ##
csvList, cellList = [], []
input_file = ''

## 메인 코드 ##
window = Tk()
window.geometry('500x100')

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='Excel 저장', command=saveExcel)


excelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='Excel 데이터 분석', menu=excelMenu)
excelMenu.add_command(label='Excel정보 보기', command=excelData01)
excelMenu.add_command(label='Excel내용 보기 - last', command=excelData02)
excelMenu.add_command(label='Excel내용 보기 - All', command=excelData03)
excelMenu.add_command(label='Excel내용 보기 - Select', command=excelData05)

window.mainloop()
#
# 10시까지 카페에 제출
# [빅데이터] 복습퀴즈. 10/11.  홍*동


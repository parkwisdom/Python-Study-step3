#(1) 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리)
#(2) 텍스트마이닝 기반 데이터 분석 (부제: 텍스트 기반 데이터 분석 및 처리)
#(3) 빅데이터 분석 결과 시각화 (부제 : 데이터베이스 기반 데이터 분석 및 GUI 시각화)
#
# 복습퀴즈1. 3개 csv 파일을 읽어서, Sales Amount의 총합계와 평균을 구한 후,
#   print()로 출력한다.
#   sales_january_2014.csv, sales_february_2014.csv, sales_march_2014.csv
# 복습퀴즈2. GUI 화면에 위 1번을 추가한다.
#   * 파일이 없으면 카페의 "CSV 처리 7 - GUI"  사용


from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import csv
import glob


def drawSheet(cList) :
    global cellList
    print(cellList)
    if cellList == None or cellList == [] :
        pass
    else :
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

def openCSV() :
    global  csvList
    csvList = []
    input_file = askopenfilename(parent=window,
                filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filereader = open(input_file, 'r', newline='')
    header = filereader.readline()
    header = header.strip()  # 앞뒤 공백제거
    header_list = header.split(',')
    csvList.append(header_list)
    for row in filereader:  # 모든행은 row에 넣고 돌리기.
        row = row.strip()
        row_list = row.split(',')
        csvList.append(row_list)

    drawSheet(csvList)

    filereader.close()

def  saveCSV() :
    global csvList
    if csvList == [] :
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',
               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')
    for  row_list  in  csvList :
        row_str = ','.join(map(str, row_list))
        filewriter.writelines(row_str + '\n')

    filewriter.close()


def csvData04():
    global csvList
    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.csv"))
    for file in file_list:
        filereader = open(file, 'r', newline='')
        csvReader = csv.reader(filereader)
        header_list = next(csvReader)
        csvList.append(header_list)
        for row in filereader:
            row = row.strip('')
            row_list = row.split(',')
            row_list[3] = row_list[3][2] + row_list[4][:len(row_list)]
            row_list[4] = row_list[5]

            csvList.append(row_list)
        filereader.close()
    drawSheet(csvList)

#전역변수
csvList, cellList = [], []

window=Tk(); window.geometry('400x400')
window.title('영상 처리&데이터 분석 Ver 1.0')

mainMenu =Menu(window); window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu=fileMenu)
fileMenu.add_command(label='CSV 열기', command=openCSV)
fileMenu.add_command(label='CSV 저장', command=saveCSV)

csvMenu = Menu(mainMenu)
mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)
csvMenu.add_command(label='여러 CSV 출력', command=csvData04)

window.mainloop()



# #
# # 복습퀴즈3(선택). RAW 파일을 분석해서 각 픽셀의 개수의 통계를 CSV파일에 저장한다.
# # 예)  lena256.raw의 분석
# # 화소값  개수
# #  0        12
# #  1        5
# #  2        33
# # ...
# # 255      77
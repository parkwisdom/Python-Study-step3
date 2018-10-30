#텍스트 파일 처리 1 (열기 --> 작업하기(내맘대로) --> 닫기)

fname = 'c:/windows/win.ini' # 원래 있는 파일
fname2='my.txt'    #복사된 원래 있는 파일

with open(fname,'r') as rfp:
    with open(fname2,'w') as wfp:

        inList = rfp.readlines()
        for inStr in inList:
            wfp.writelines(inStr)


        # inStr = rfp.readlines()
        # if inStr == ''or inStr==None: #if not inStr
        #     break
        # # print(inStr,end='')
        # wfp.writelines(inStr)

rfp.close()
wfp.close()
print('ok')

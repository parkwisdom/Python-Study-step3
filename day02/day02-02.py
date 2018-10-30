#시 또는 소설등의 빅데이터에서 빈도 분석하고 순위 매기기

inStr = """꽃게가 간장 속에
반쯤 몸을 담그고 엎드려 있다
등판에는 간장이 울컥울컥 쏟아질 때
꽃게는 뱃속의 알을 껴안으려고
꿈틀거리다가 더 낮게
더 바닥쪽으로 웅크렸으리라
버둥거렸으리라 버둥거리다가
어찌할 수 없어서
살 속으로 스며드는 것을
한 때의 어스름을
꽃게는 천천히 받아들였으리라
껍질이 먹먹해지기 전에
가만히 알들에게 말했으리라
저녁이야
불 끄고 잘 시간이야
"""
import operator
pDic ={}
pList =[]
totalRank, currentRank =1,1


for i in inStr:
    if '가'<= i and i <='힣':
        if i in pDic:
            pDic[i]+=1
        else:
            pDic[i]=1
print(pDic)
pList = sorted(pDic.items(),key=operator.itemgetter(1),reverse=True) # 딕셔너리의 1번째 자리 기준으로 정렬

print(pList[0],1)
for i in range(1,len(pList)):
    totalRank+=1
    if pList[i][1]==pList[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(pList[i], currentRank)

strList = inStr.split()
print(strList)

countDic ={}
for data in strList:
    if data[-1] in ['.',',','가']:
        data = data[:-1]

    if data in countDic:
        countDic[data]+=1
    else:
        countDic[data]=1
print(countDic)
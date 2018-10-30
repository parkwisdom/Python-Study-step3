import operator

ttList=[('토마스',5),('헨리',8),('에드워드',9),('토마스',4),('헨리',2)]

tDic, tList = {},{}
totalRank, currentRank =1,1

#메인코드
for tmpTup in ttList :
    tName= tmpTup[0] #기차이름 : 키
    tWeight = tmpTup[1] #기차 작업량
    if tName in tDic:
        tDic[tName] += tWeight
    else:
        tDic[tName]=tWeight

tList = sorted(tDic.items(),key=operator.itemgetter(1),reverse=True) # 딕셔너리의 1번째 자리 기준으로 정렬

print(tList[0],currentRank)
for i in range(1,len(tList)):
    totalRank+=1
    if tList[i][1]==tList[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(tList[i], currentRank)

print(tDic)
print(tDic.items())
print(tList)

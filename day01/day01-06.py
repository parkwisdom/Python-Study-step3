#리스트 연습
#
# myList = []
# myList.append(10)
# myList.append('20')
# myList.append([1,2,3])
#
# print(myList)

#로또 추첨
import random

lotto = []
for i in range(6):
    num = random.randint(1,45)
    if lotto.count(num)>0:
        continue
    lotto.append(num)
    if len(lotto)>= 6:
        break
lotto.sort()
print(lotto)
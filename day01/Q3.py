ROW = int(input("행-->"))
COl = int(input("열-->"))

myList=[]
tmpList=[]
for i in range(ROW):
    tmpList=[]

    for k in range(COl):
        k+=COl*i+1
        tmpList.append(k)
    myList.append(tmpList)

print(myList)


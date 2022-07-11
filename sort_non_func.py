list = [100,12,10,-10,0.5,0.1,12.3]
sortList = []
#i = 0
while list:
    firstIndex = list[0]
    for i in list:
        #firstIndex = list[0]
        # secondIndex = list.index(100.0, firstIndex + 1)
        if firstIndex > i:
            firstIndex = i
    sortList.append(firstIndex)
    list.remove(firstIndex)
        
print(sortList)
    
        
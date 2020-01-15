#LIST

aList = [1,2,3,4,5]
bList = []

#print aList
#print bList

a = aList[3]
#print aList

#assigning a new value to the list
aList[1] = 20
#print aList


bList.append(10)
bList.append(20)
bList.append(30)
#print bList

#extend
#aList.extend(bList)
#print aList

#adding two lists
cList = aList + bList
#print cList

#insert
dList = [2,4,6,8,0]
dList.insert(3, "awkward string in the middle")
print dList

#pass the index to pop to delete the value form list
dList.pop(3)
print dList

#remove removes by value (not by index)
dList.remove(8)
print dList


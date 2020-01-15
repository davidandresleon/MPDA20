#nested loops

listOfList = [ [6,1,2,5,6] , [ "a", "b", "c"] ]

#print listOfList[0]
#print type(listOfList[0])


"""
for i in listOfList:
    #print i
    #print range(len(i))
    for j in range(len(i)):
        print i[j]
"""


for subList in range(len(listOfList)):
    for item in listOfList[subList]:
        print item

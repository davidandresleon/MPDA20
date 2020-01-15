#FOR LOOPS

#RANGES
aList = [] #empty list
aList = [1,2,3,4,5]

#print range(10)
#print range(10,20)
#print range(0,20,2)

bList = range(10,0, -2)
#print bList
#print type(bList)
#print len(bList)


#FOR LOOPS

studentList = ["Juan", "Omar", "Fares"]
#studentIndx = range(len(studentList))

for i in range(len(studentList)-1):
    print studentList[i], studentList[i+1] 


for i in range(len(studentList)):
    if i+1 < len(studentList):
        print studentList[i], studentList[i+1] 




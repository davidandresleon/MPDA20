#list slices

aList = [1,2,3,4,5]

#reference a list
bList = aList

aList[1] = 1000

#copy a list into a NEW ONE 
cList = aList[:]
#print cList

dList = [1,2,3,4,5,6,7]

#from index 3 forth
eList = dList[3:]
print eList

#first items before index 4
fList = dList[:4]
print fList

#take items from index two to five (not including)
gList = dList[2:5]
print gList








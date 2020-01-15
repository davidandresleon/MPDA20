#FUNCTIONS


def add(number1, number2):
    sum = number1 + number2
    
    """ whatever you do here"""
    return sum

a = add(10,20)
print a

#non-fruitful
def changeFirstValue(list):
    list[0] = 0

aList = [2,3,4,5]
print aList

changeFirstValue(aList)
print aList


#----------------------------------------



#non-fruitful
def changeValue(var):
    var = 0

#value doesnt get changed because its copyied
a= 1000
changeValue(a)
print a



#everyTimeThereIsAChangeOfWord -> camelcase
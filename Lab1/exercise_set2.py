"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    list3 = [listOne[1]]
    for el in listTwo:
        list3.append(el)



# ex2
def exercise2():
    sampleList = [34, 54, 67, 89, 11, 43, 94]
    a =sampleList[4]
    sampleList.pop(4)
    sampleList[2] = sampleList[2]+a
    sampleList[len(sampleList)-1] = sampleList[len(sampleList)-1]+a



# ex3
def exercise3():
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    a=list()
    for i in range(0,3):
        a.append(sampleList[3*i:3*i+int(len(sampleList)/3)])
    for el in a:
        el.reverse()




# ex4
def exercise4():
    sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    a = {}
    for el in sampleList:
        if el not in a.keys():
            a[el]=1
        else:
            a[el] +=1


# ex5
def exercise5():
    firstList = [2, 3, 4, 5, 6, 7, 8]
    secondList = [4, 9, 16, 25, 36, 49, 64]
    a = set()
    for el in firstList:
        a.add(el)
    for el in secondList:
        a.add(el)


# ex6
def exercise6():
    firstSet = {23, 42, 65, 57, 78, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    d = firstSet.intersection(secondSet)
    firstSet=firstSet-d




# ex7
def exercise7():
    firstSet = {57, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    flag=1
    for el in firstSet:
        if el not in secondSet:
            flag=0
    if flag==1:
        secondSet=secondSet-firstSet

# ex8
def exercise8():
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    x = set()
    for el in rollNumber:
        if el not in sampleDict.values():
            x.add(el)
    for el in x:
        rollNumber.remove(el)



# ex9
def exercise9():
    speed = {'Jan ':47 , 'Feb ':52 , 'March ':47 , 'April ':44 , 'May ':52 ,'June ':53 , 'July ':54 , 'Aug ':44 , 'Sept ':54}
    a = set()
    for el in speed:
        a.add(speed[el])
    b = list(a)





# ex10
def exercise10():
    sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
    list2=list()
    for el in sampleList:
        if el not in list2:
            list2.append(el)
    t = (min(list2),max(list2))



if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()

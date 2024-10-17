"""Exercise Set 3: Numpy Exercises"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    a = np.arange(8).reshape(4,2)
    print(a)
    a = a.shape, a.dtype, a.size
    print("1. Attributes of 4x2 array:", a)


# ex2
def exercise2():
    a = np.arange(100,200,10).reshape(5,2)
    print(a)


# ex3
def exercise3():
    a=np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
    b = a[:,2]
    print(b)

# ex4
def exercise4():
    a=np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48]])
    b = np.zeros(a.shape)
    for i in range(4):
        if i%2==0:
            b[i,:] = a[:,i]
        else:
            b[i,:] = a[i,:]
    print(b)


# ex5
def exercise5():
    a=np.array([[5, 6, 9], [21 ,18, 27]])
    b=np.array([[15 ,33, 24], [4 ,7, 1]])
    c=np.sqrt(a+b)
    print(c)



# ex6
def exercise6():
    a=np.array([[34,43,73],[82,22,12],[53,94,66]])
    a.sort()
    print(a)


# ex7
def exercise7():
    a=np.array([[34,43,73],[82,22,12],[53,94,66]])
    print(a.max(0),a.min(1))


# ex8
def exercise8():
    a=np.array([[34,43,73],[82,22,12],[53,94,66]])
    b = np.array([10,10,10])
    a[:,1]=b
    print(a)




if __name__ == "__main__":
    print("EXERCISE SET 3: NumPy Exercises")
    print("EX1")
    #exercise1()
    print("EX2")
    #exercise2()
    print("EX3")
    #exercise3()
    print("EX4")
    #exercise4()
    print("EX5")
    #exercise5()
    print("EX6")
    #exercise6()
    print("EX7")
    #exercise7()
    print("EX8")
    exercise8()

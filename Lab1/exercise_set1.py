"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    a = int(input("inserisci a:"))
    b = int(input("inserisci b:"))
    if(a*b > 1000):
        return a+b
    return a*b



# ex2
def exercise2():
    x = range(3, 9)
    i = 8
    for k in range(i,len(x)):
        print(x[k]+x[k-1])



# ex3
def exercise3():
    x = list(range(3, 9))
    x.append(3)
    if x[0] == x[len(x)-1]:
        return(True)
    else:
        return(False)



# ex4
def exercise4():
    x = list(range(5,900,9))
    for el in x:
        if el%5==0:
            print(el)


# ex5
def exercise5():
     x = "Emma is a good developer. Emma is also a writer"
     k = x.split(" ")
     cnt =0;
     for parola in k:
         if parola == "Emma":
             cnt +=1
     return cnt



# ex6
def exercise6():
    a = list(range(1,10))
    b = list(range(11,20))
    c = list()
    for i in range(0,len(a)-1):
        if a[i]%2 ==1:
            c.append(a[i])
    for i in range(0,len(b)-1):
        if b[i]%2 ==0:
            c.append(b[i])



# ex7
def exercise7():
    a = "casetta"
    b = "albero"
    c = a[0:int(len(a)/2)] + b + a[int(len(a)/2):len(a)]



# ex8
def exercise8():
    a = "casetta"
    b = "albero"
    c = a[0] + a[int(len(a)/2)] + a[len(a)-1] + b[0] + b[int(len(b)/2)] + b[len(b)-1]
    return c


# ex9
def exercise9():
    a = "agdvdGCFHTD%/&("
    d = 0
    u =0
    l=0
    s=0
    for letter in a:
        if letter.islower():
            l+=1
        elif letter.isupper():
            u+=1
        elif letter.isdigit():
            d+=1
        else:
            s+=1
    print(d,u,l,s)


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
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
    #exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()

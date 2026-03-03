n = 3

# for i in range(1,n+1):
#     print("*"*i)

# for i in range(1,n+1):
#     print(" " * (n-i)+ "*" *(2*i-1))

# for i in range(1,n+1):
#     print("*" * (2*i-1) + " " * (n-i))



# n = 3  

# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# for i in range(2, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))


# n=3
# for i in range(1, n+1):
#         print("*" * i)
# for i in range(n-1, 0, -1):
#         print("*" * i)

# n = 4

# for i in range(1, n + 1):
    
#     print("*" * i, end="")
    
#     print(" " * (2 * (n - i)), end="")
    
#     print("*" * i)




# n = 5

# for i in range(n, 0, -1):
#     print(" * " * i)



# i = 5
# while i<=5:
#     print(" * " * i)
#     i+=1



#functions 
# def show ():
#     print("hell world")
# show()


def sayhello ():
    print("if u have guds catch me")
sayhello()



def hello(name, age,sal):
    print("hi",name,"your age is :",age,"your sal is :",sal)
hello("shrikar",43,3000000)
hello("sarthak",1,4000000)




def printMax(a,b):
    if a>b:
       print(a, 'is maximum')
    elif a== b:
        print(a, 'is equal to',b)
    else:(b, 'is maximum')
printMax(7,5)


def numbers(*num):
    print(num)
numbers(1,2,3,4,5)



def myFun(*argv):
    for i in argv:
        print(i)
        
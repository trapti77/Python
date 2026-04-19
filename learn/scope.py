x=99

# def fun3():
#     global x
#     x=12
#     print(x)

# fun3()
# print(x)


# def f1():
#     x=88
#     def f2():
#         print(x)
#     f2()
# f1()


# def f1():
#     x=88-----------------
#     def f2():            | 
#         print(x)         closure   
#     return f2------------|
# myResult=f1() 

# myResult()

def chaiaurcode(num):
    def actual(x):
        return x**num
    return actual

f=chaiaurcode(2)
g=chaiaurcode(3)

# different memory address 
print(f(3))
print(g(3))
   
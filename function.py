"""def calculatemean(a,b):
    mean=(a*b)/(a+b)
    print(mean)



a=9
b=8
calculatemean(a,b)
#gmean=(a*b)/(a+b)
#print(gmean)
c=8
d=7
calculatemean(c,d)
#gmean2=(c*d)/(c+d)
#print(gmean2)
def greater(a,b):
    if(a>b):
        print(a,"isgreater")
    else:
        print(b,"is greater")

def lesser(a,b):
    pass

a=8
b=10
greater(a,b)


c=7
d=5
greater(c,d)"""
#---------------------------------------------->function argument<---------------------------------------
#-----------1--->required argument-------------
#def average(a,b):
def average(a=9,b=1):
    print("the average =",(a+b)/2)


#average(4,6)

#----------------2---defualt argument-----------
average()
#average(4,2)
#average(4)
#average(b=9)
#----------------3---keyword argument------------
average(b=8,a=8)
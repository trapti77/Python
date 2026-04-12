
print("=========================================CALCULATOR=======================================")
x=input("enter the first number:")
y=input("enter the second number:")
#here this input function take every input as a string 
#so we are need to convert it into integer using typecasting functions
print("number1=",x+"\n numer2=",y)
print("addition of two numer=",int(x)+int(y))
print("substraction of two numer=",int(x)-int(y))
print("multiplication of two numer=",int(x)*int(y))
print("division of two numer=",int(x)/int(y))
print("remender of two numer=",int(x)%int(y))
print("floor division of two numer=",int(x)//int(y))
print("exponential of two numer=",int(x)**int(y))
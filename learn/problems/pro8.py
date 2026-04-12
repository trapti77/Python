#Reverse a string 

str=input("Enter String :")
revstr=""
notrevstr=""

for char in str:
    revstr=char+revstr
    
print("Reverse string :",revstr)


for char in str:
    notrevstr=notrevstr+char
    
print("Not Reverse string :",notrevstr)
    
        

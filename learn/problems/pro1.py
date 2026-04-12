age=int(input("Enter Age : "))

print("type of age : ",type(age))

if age<13 :
    print("Child")
elif age>=13 and age<19:
    print("Teenager")
elif age>=19 and age<59:
    print("Adult")
else:
    print("Senior")
    
    
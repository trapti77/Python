# Keep asking number untill user enter number btw 1-10


while True:
    number=int(input("Enter number :"))
    print("Your number is : ",number)
    if number>=1 and number<=10:
        break
    else:
        print("invalid number please enter again")
    

        

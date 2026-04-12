# First non repeating char

str=input("Enter String :")

for char in str:
    if str.count(char)==1:
        print("first non repeat char : ",char)
        break
    

        

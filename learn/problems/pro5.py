# num=int(input("Enter Number : "))

# for n in range(num):
#     print(n)

#Count positive number in list

nums=[-1,3,4,-3,5,3,-1,2,2,2]
c=0

for num in nums:
    if num >=0:
        c+=1
        
print("Total Positive Number : ",c)
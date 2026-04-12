#Sum of even number

nums=10
sum=0

for num in range(nums):
    if num%2==0:
        sum+=num
        
print("Sum Of Even Numbers : ",sum)
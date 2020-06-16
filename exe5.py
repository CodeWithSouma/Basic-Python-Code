# sum of n natural numbers
# ask a user for natural number(n) 
# print total from 1 to n

sum=0
n=int (input ("enter how many natural number you want to sum: ")) 
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(f"sum {i-n} to {n}: "+str(sum))
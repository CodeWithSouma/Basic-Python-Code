# practice for loop
# ask user a number like 1234
# calculate sum of digits  1+2+3+4

num =input("enter a number: ")
len=len(num)
sum=0
for i in range(len):
    sum+=int(num[i])
print("sum of digits: "+str(sum))
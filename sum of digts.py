# # sum of dgits
# sum=0
# digit=0
 
# num=input ("enter a number: ")
# num=int(num)
# while num>0:
#     digit=int(num)%10
#     sum=sum+digit
#     num=int(num)/10
# print("sum of digits: "+str(sum))


# another methord to solve this problem
num=input("enter a number:")
sum=0
i=0
while i<len(num):
    sum=sum+int(num[i])
    i+=1
print("result:"+str(sum))


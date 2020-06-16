print("the armstrong number between 1 to 1000 = ")
for i in range(1001):
    num=i
    n=i
    l=len(str(num))
    sum=0
    r=0
    while(n!=0):
        r=n%10
        sum=sum+r**l
        n=n//10
    if(sum==num):
        print(f"{num}",end=" ")
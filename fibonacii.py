a=0
b=1
n=int(input("enter range: "))
print("printing fibonacii series:",end=" ")
print(a,end=" ")
print(b,end=" ")

for i in range(1,n-1):
    fibo=a+b
    print(fibo,end=" ")
    a=b
    b=fibo
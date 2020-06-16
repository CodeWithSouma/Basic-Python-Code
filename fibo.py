
# fibonaci series
# 0 1 1 2  3 5 8 13 21 34

# for i in range (1,11):
#     print(i,end=" ")


def fibonacci_seq(n):
    a=0# first number
    b=1# second number
    fibo=1
    if n==1:
        print(a)
    elif n==2:
        print(a,end=" ")
        print(b,end=" ")

    else:
        print(a,b, end=" ")
        for i in range(n-2):
            fibo=a+b  
            print(fibo,end=" ")
            a=b
            b=fibo
            i+=1


num=int(input("enter how many number you want to prnt in fibonacci series:"))
fibonacci_seq(num)
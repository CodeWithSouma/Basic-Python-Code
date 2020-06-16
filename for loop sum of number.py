# sum from 1 to 10
# 1+2+3........................10
while True:
    sum=0
    n=int(input ("how many number you want to sum enter the range: "))
    for i in range (1,n+1):
        sum =sum+i
    print(f"result of sum: {sum}")
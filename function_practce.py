# # function practice
# def function(name):
#     return name[-1]

# name=input("enter your name:")

# ch=function(name)
# print(ch)

def even_odd(num):
    if num%2==0:
        print("even.")
    elif num%2!=0:
        print("odd")
while True:
    n=int(input("enter a number: "))
    even_odd(n)
# if elif else statement

# show ticket pricing 
# 0 to 3 free
# 4 to 10  150
# 11 to 60  250
# bove 60 200

age=int(input ("enter your age: "))
if (age>=0 and age<=3):
    print("free")
elif(age>=4 and age<=10):
    print("you have to pay 150")
elif (age>=11 and age<=60):
    print("you havve to pay 250")
elif(age>60):
    print("you have to pay 200")
else :
    print("invalid input")


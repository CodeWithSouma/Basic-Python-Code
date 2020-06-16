# practice for loop
# ask user name and count each character 
# "soumadip"
# s=1
# o=1
# u=1
# m=1
# a=1
# d=1
# i=1
# p=1

name=input("enter yor name: ")
temp=""
for i in range(0,len(name)):
    if name[i] not in temp :
        temp+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
# # center methord
# name= "soumadip"
# # **soumadip** *for space
# print(name.center(len(name)+4,"*"))
# print(len(name))

user_name,star=input("enter user name and how many star you want print(seperated by comma):").split(",")
print(user_name.center(len(user_name)+int(star),"*"))
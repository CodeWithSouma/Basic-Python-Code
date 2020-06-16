# replace() methord
# find() methord


string ="is she is beautyful and she is good dancer"
after_replace=string.replace("is","was",1)# for only first is replace if you want both is replace with was
# you must be use 2 or nothing after passing was parameter 
print("before replace: "+string)
print(f"after replace: {after_replace}")

possition=string.find("is",8)# i want to count second is position
print("position of is : "+str(possition))



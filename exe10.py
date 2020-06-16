# def reverse_list(l):
#      l.reverse()
#      return l


# def reverse_list(l):
#     return l[::-1]

def revli(l):
    r_list=[]
    for i in range(0,len(l)):
        poped=l.pop()
        r_list.append(poped)
    return r_list



number=list(range(1,11))

li=revli(number)

# print(reverse_list(number))
print(li)
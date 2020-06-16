# number gussing game
# make a variable, like winning_number and assign any number to it.
# ask user to gussed a number
# if user guessed correctly then print "YOU WIN !!!!"
# if user did not gussed correctly then :
          # if user gussed lower than actual number then print "too low"
          # if user gussed higher than actual number then print "too high"
# goole "how to geneate random number in python " to genete random
# winning number 

#*************************************************************#
#                       number gussing game                   #
#*************************************************************#

import random
count=1
winning_number=random.randint(1,10)
while True:
    if count==1:
        gussed_number=int (input("enter a number between 1 to 10 : ") )
    else:
        gussed_number=int (input("Try again!!!enter a number between 1 to 10 : ") )
    if winning_number==gussed_number:
        
        print(f"Hurra. you win !!!,and you have gussed this number in {count} times")
        break
    elif (winning_number>gussed_number ):
        print("too low.\n")
        count+=1
    elif (winning_number<gussed_number) :
        print("too high.\n")
        count+=1


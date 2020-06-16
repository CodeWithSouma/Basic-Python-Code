# take two comma seperated input from user 
# user's name 
# a single character 


# output - 2 print lines
# user's name length 
# count the character that user inputed (bonus : case insensitive count )


user_name,single_character=input("enter your name and a single character : ").split(",")
print(f"user name length: {len(user_name.strip())}")
print(f"count of the \"{single_character.strip()}\" that user  inputed:{(user_name.strip().upper()).count(single_character.strip().upper())}")

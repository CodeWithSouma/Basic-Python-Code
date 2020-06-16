def is_palindrom(word):
    reversed_word=word[::-1]
    if reversed_word==word:
        return "palindrom"
    else:
        return "not palindrom"

    




word=input("enter a string: ")    
print(is_palindrom(word))
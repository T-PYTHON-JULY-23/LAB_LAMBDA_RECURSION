'''Q1) Using recursion, if given a word/phrase return how many vowels
(a,e,i,o,u) are in that phrase or word:'''
def number_of_vowels (word:str) :
    
    vowels= ['a','e','i','o','u']
    if not word:
       return 0
    elif word[0].upper().lower() in vowels:
        return 1 + number_of_vowels(word[1:])
    else:
        return 0 + number_of_vowels(word[1:])


sentence = number_of_vowels("IF YOU DON'T BELONG DON'T BE LONG")
print(sentence)






'''Q2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton'''
list_numbers = [40,35, 10, 15, 20]
A_numbers = map(lambda num: num* num , list_numbers)
print(list(A_numbers))
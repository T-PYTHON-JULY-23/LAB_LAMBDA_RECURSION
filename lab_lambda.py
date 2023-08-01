#Q1
def phrase_vowels (word:str) -> int:
    'return the number of vowels in word using a recursive computation'
    vowels= ['a','e','i','o','u']

    if not word:
        return 0
    elif word[0].upper().lower() in vowels:
        return 1 + phrase_vowels(word[1:])
    else:
        return 0 + phrase_vowels(word[1:])


phrase = phrase_vowels("I love python")
print(phrase)



#Q2
numbers = [40,35, 10, 15, 20]
odd_numbers = map(lambda num: num* num , numbers)
print(list(odd_numbers))



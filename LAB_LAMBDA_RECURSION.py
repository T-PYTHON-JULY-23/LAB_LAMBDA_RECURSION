#Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

def vowels_char_count(vowels):
    if not vowels:
        return 0
    return 'aeiouAEIOU'.count(vowels[0]) + vowels_char_count(vowels[1:])

print(f"vowels character that is in phrase : ", vowels_char_count("I love python"))

# Given a list of numbers : [40,35, 10, 15, 20],  create a new list containing each number from the previous list mutliplied by itself.
list_number = [40,35, 10, 15, 20]
mutliplied_list = map(lambda x : x*x , list_number)
print(list(mutliplied_list))


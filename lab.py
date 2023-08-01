#1
def how_many_vowels(phrase): 
    vowels_litters = ("a","e","i","o","u")
    word = phrase.lower()
    if len(phrase) ==0: 
        return 0 
    elif phrase[0] in vowels_litters:
        return 1+ how_many_vowels(phrase[1:])
    else: 
        return how_many_vowels(phrase[1:])

print (how_many_vowels("i love python"))


#2

numbers = [40,35, 10, 15, 20]
 
mutliplition = list(map(lambda x:x*x ,numbers))
print(mutliplition)
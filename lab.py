#1
def phrase(word): 
    vowels = ("a","e","i","o","u")
    word = word.lower()
    if len(word) ==0: 
        return 0 
    elif word[0] in vowels:
        return 1+ phrase(word[1:])
    else: 
        return phrase(word[1:])

print (phrase("i love python"))


#2

numbers = [40,35, 10, 15, 20]
 
multiblation = list(map(lambda x:x*x ,numbers))
print(multiblation)
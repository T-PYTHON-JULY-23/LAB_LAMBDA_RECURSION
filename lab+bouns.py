#1

def many_vowels(word):
   
    vowels=['a','e','i','o','u']
    word = word.lower()
    if len(word) ==0:
        return 0
    elif word[0] in vowels:
        return 1 + many_vowels(word[1:])
    else:
        return many_vowels(word[1:])
    
print(many_vowels("I love python"))   
        
#2
number=[40,35, 10, 15, 20]
squae_number=list(map(lambda X:X*X,number))
print(squae_number)
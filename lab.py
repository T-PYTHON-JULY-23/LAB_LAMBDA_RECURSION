def vowels_counter( phrase:str ) -> int:
    '''this function will count all the vowels in the phrase and print the vowels count in the phrase'''

    if len(phrase) == 0:
        return 0
    
    chr = phrase[-1].lower()
    
    if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
        return 1 + vowels_counter(phrase[:-1])
    else:
        return vowels_counter(phrase[:-1])

my_list = [40,35, 10, 15, 20]

mult_my_list = list(map(lambda num : num*num, my_list))

print(mult_my_list)
print(vowels_counter("I love python"))


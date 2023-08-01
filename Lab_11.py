
def vowels_count(phrase ):
    ''' Return number of vowels in string '''
    if len(phrase ) == 0:
        return 0
    letter = phrase [0]
    if letter in 'aeiouAEIOU':
        return 1 + vowels_count(phrase [1:])
    return vowels_count(phrase [1:])

print(vowels_count.__doc__)
print (vowels_count('I love python'))
print("-"*10)


# create a new list containing each number from the previous list mutliplied by itself.
numbers = [40,35, 10, 15, 20]


result = map(lambda x: x * x, numbers)
print(numbers)
print("The new list containing each number from the previous list mutliplied by itself.")
print(list(result))


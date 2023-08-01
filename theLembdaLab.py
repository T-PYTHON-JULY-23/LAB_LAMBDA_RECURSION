#Q1

def vowel_counter(sentence):
     if len(sentence)==0 or sentence==None:
        return 0
     if sentence[0].lower() in ['o','a','i','e','u']:
        return 1 + vowel_counter(sentence[1:])
     else:
        return vowel_counter(sentence[1:])

print(f"number of vowels is: {vowel_counter('I love python')}\n")


#Q2  

def subtract(n):
	return n * n

numbers = [40,35,10,15,20]
print("App to multiplying each number in the list by itself ")
print(f"Original list: {numbers}")

result = map(subtract, numbers)
print(f"List after multiplied: {list(result)}")
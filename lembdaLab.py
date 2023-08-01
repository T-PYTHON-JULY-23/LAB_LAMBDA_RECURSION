#Q1
"""def vowels (sentence):
     sentence=sentence.lower
     vowel=["a","e","i","o","u"]
     lst = []
     count=0
     for letter in sentence():
         lst.append(letter)
        
     for n in lst:
        if lst[n]==vowel:
             count+=n
        return count + vowels(sentence)
vowels("Hello my")
"""
#Q2  DDDDOOOONNNNEEEE
def subtract(n):
	return n * n
numbers = [40,35,10,15,20]
print("App to multiplying each number in the list by itself ")
print(f"Original list: {numbers}")

result = map(subtract, numbers)
print(f"List after multiplied: {list(result)}")


"""def vowels (sentence):
     sentence=sentence.lower
     vowel=["a","e","i","o","u"]
     lst = []
     count=0
     for letter in sentence():
         lst.append(letter)
         if vowel in lst:
             count+=
     return count + vowels(sentence)
vowels("Hello my")

"""
sentence="my name is "
vowels=["a","e","i","o","u"]
vowel=sentence.find
print(vowel)
#Q1

def vowel_counter(phrase):
     list=['o','a','i','e','u']
     if len(phrase)==0 or phrase==None:
        return 0
     if phrase[0].lower() in list:
        return 1 + vowel_counter(phrase[1:])
     else:
        return vowel_counter(phrase[1:])
     
print(f"Counts of vowels in this phrase:  {vowel_counter('I love python')}\n")

#Q2  

def subtract(n):return n * n
numbers = [40,35,10,15,20]
result = map(subtract, numbers)
print(f"Multiplying each number in this list: {numbers}")
print(f"List after multiplied: {list(result)}")




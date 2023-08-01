# LAB_LAMBDA_RECURSION
# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
# Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
# Example: given the phrase I love python , it should return : 4
def vowels_count(word:str):
        vowels = "aeiouAEIOU"
        if word == "":
             return 0 
        
        elif word[0] in vowels:
              return 1 + vowels_count(word[1:])
        else:
              return vowels_count(word[1:])
   
print(vowels_count("I love python"))



# 2) Given a list of numbers : [40,35, 10, 15, 20]
# create a new list containing each number from the previous list mutliplied by itself.
lst = [40,35, 10, 15, 20]
# print the new list.
New_list = list(map(lambda x : x * x , lst))
print(New_list)
# Hint: use map() with a lambda funciton
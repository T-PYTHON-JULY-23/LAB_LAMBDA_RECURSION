#lab Lamda Recursion


#Q1 
  
word = input("write a phrase to count the vowels: ")

def countVowels(word):

    if len(word) == 0:
        return 0
    else: 
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            return 1 + countVowels(word[1:])
        else:
            return countVowels(word[1:])
        
    
print("the number of vowels in the sentence:", word, "is",countVowels(word))




#Q2

myList = [40,35, 10, 15, 20]
mutlipliedNumList = list(map(lambda x : x*x, myList))
print(mutlipliedNumList)


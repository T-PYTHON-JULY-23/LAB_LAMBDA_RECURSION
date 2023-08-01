# Q1

def isVowel(alpha):
    return alpha.lower() in ['a','e','i','o','u']
  
def How_Many_Vowels(words , length):
    
    if length == 0:
        return 0
    elif length == 1:
        return isVowel(words[length-1])
    else:
        return isVowel(words[length-1])+ How_Many_Vowels(words,length-1)



# Q1
word = "I love python"

print (f"given the phrase {word} , the nimber of vowels :{(How_Many_Vowels(word,len(word)))}")

print("-"*20)

# Q2
numbers = [40,35,10,15,20]
final_number= list (map(lambda number: number*number, numbers))

print(f" given the list {numbers} mutliplied each number by itself: {final_number}")


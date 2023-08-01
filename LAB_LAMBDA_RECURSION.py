

def isVowel(ch): 
  vowels = "aeiou" 
  ch = ch.lower() 

  if ch in vowels: 
    return 1
  else:
      return 0

def countVowels(word, ln): 

   if ln == 0 :
     return 0
   if ln==1:
      return isVowel(word[0])
   
   return countVowels(word, ln - 1) + isVowel(word[ln - 1])
                       

word = input("Enter a word: ")

print(countVowels(word, len(word))) 

new_list=[40,35, 10, 15, 20]
muliplied_list = map(lambda item: item*item, new_list)
print(list(muliplied_list))
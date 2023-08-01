






def num_vowels (phrase:str):

    #user = input("given the phrase:")

    vowels ="a", "e", "i", "o " , "u"
    count = 0
    
    if len(phrase) == 0 :
       return 0
       
    phrase.count(vowels)
    count+=1
    len(phrase)-1
    
       
    return count + num_vowels(phrase)

print (num_vowels("I love python"))








 #lambda funciton

list_of_numbers=[40,35, 10, 15, 20]

print(list(map(lambda numbers : numbers * numbers ,list_of_numbers )))


print("_"*50)
#for loop

for i in list_of_numbers:
   new_list= i*i 
   print(new_list)

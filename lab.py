
#1) Using recursion, if given a word/phrase return how many
# vowels(a,e,i,o,u) are in that phrase or word:
def is_vowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']

def count_vowels(string, length_string):
    if (length_string== 1):
        return is_vowel(string[length_string - 1])
    return (count_vowels(string, length_string - 1) +
                is_vowel(string[length_string - 1]))


phrase = "I love python"


print(" numbers of Vowel is : ",count_vowels(phrase, len(phrase)))

#2) Given a list of numbers : [40,35, 10, 15, 20]
num=[40,35, 10, 15, 20]

print("list befor ",num,"list mutliplied by itself",list( map((lambda x : x*x),num)))

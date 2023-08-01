#Q1
def vowelsCount(phrase):
   vowels = 'aeiouAEIOU'
   if phrase == '':
      return 0
   elif phrase[0] in vowels:
      return 1 + vowelsCount(phrase[1:])
   else:
      return 0 + vowelsCount(phrase[1:])
print('-------Q1-------')
print(vowelsCount('I love python'))
#Q2 
print('-------Q2-------')
myList = [40,35, 10, 15, 20]
mutlipliList= map(lambda elemnt:elemnt*elemnt, myList)
print(list(mutlipliList))

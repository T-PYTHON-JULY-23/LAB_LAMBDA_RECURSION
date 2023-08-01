##Q1 :
def recVowelCount(i):
    if not i:
        return 0
    return 'aAeEiIoOuU'.count(i[0]) + recVowelCount(i[1:])
count_result = recVowelCount("I love python")
print(count_result)
##Q2 :
my_list =[40,35, 10, 15, 20]
result = map(lambda number : number * number ,my_list)
print(list(result))
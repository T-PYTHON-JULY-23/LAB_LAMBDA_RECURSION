
def recurison(chr:str) -> str:
    vowels = "aeiou"
    # chr_low= chr.lower
    if len(chr) == 0 :
        return 0
    elif chr[0].lower() in vowels:
        return 1 + recurison(chr[1:])
    else:
        return  recurison(chr[1:])
result = recurison("I love python")
print(result)


list1 = [40,35, 10, 15, 20]
print(list1)

multi_list = map(lambda x,: x*x ,list1)
print(list(multi_list))



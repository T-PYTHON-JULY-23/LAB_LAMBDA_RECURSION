print("-"*30)
print("FizzBuzz using for")
print("-"*30)
for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        continue
    elif number % 3 == 0:
        print("Fizz")
        continue
    elif number % 5 == 0:
        print("Buzz")
        continue
    print(number)
   
print("-"*30)
print("FizzBuzz using loop")
print("-"*30)
i=1
num=100
while (i < num):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif  i % 3 == 0:
        print('Fizz')
    elif  i % 5 == 0:
        print("Buzz")
    
    else:
        print(i)
    i += 1
    
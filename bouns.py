def for_fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num% 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

def while_fizzbuzz():
    count = 0
    while count < 101:
        if count % 5 == 0 and count % 3 == 0:
            print ("FizzBuzz")
            count = count +1
        elif count % 3 == 0:
            print ("Fizz")
            count = count + 1
        elif count % 5 == 0:
            print ("Buzz")
            count = count +1
        else:
            print (count)
            count = count + 1
      



print("fizzbuzz by For loop : ")
for_fizzbuzz()

print("-"*30)


print(f"fizzbuzz by While loop :")
while_fizzbuzz()

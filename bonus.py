def FizzBuzz ():
    for numbers in range(1,100):
        if numbers % 3 == 0 and numbers % 5 == 0 :
            print(f"{numbers} : FizzBuzz")
        elif numbers % 5 == 0 :
            print(f"{numbers} : Buzz")
        elif numbers % 3 == 0 :
            print (f"{numbers} : Fizz")
FizzBuzz()
print ("--------------------the same program using a while loop instead--------------------")
number = 1
while number in range(1,100):
    if number % 3 == 0 and number % 5 == 0 :
            print(f"{number} : FizzBuzz")
    elif number % 5 == 0 :
            print(f"{number} : Buzz")
    elif number % 3 == 0 :
            print (f"{number} : Fizz")
    number +=1
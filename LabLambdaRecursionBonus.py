#lab Lambda Recursion bonus

# using for 
def FizzBuzzFor():
    for i in range(1,101):
        if i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

FizzBuzzFor() 


# using while 
def FizzBuzzWhile():
    i = 1
    while i <= 100:
        if i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
        i+=1

FizzBuzzWhile()





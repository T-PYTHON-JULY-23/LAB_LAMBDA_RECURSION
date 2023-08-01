def for_check_fizzbuzz():
    for num in range (0,100+1):
        if num % 3 == 0 and num % 5 == 0:
          print("FizzBuzz")
        elif num % 5 == 0:
         print("Buzz")
        elif num % 3 == 0:
         print( "Fizz")
        else:
         print(num)
for_check_fizzbuzz()


def while_check_fizzbuzz():
    num =1 
    while num <= 100:
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%5==0:
            print("Buzz")
        elif num%3==0:
            print(" Fizz ")
        else :
            print(num)
        num+=1 
while_check_fizzbuzz()
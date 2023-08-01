def fizzbuzz_for(times):
    for num in range(1, times + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz!!")
        elif num % 3 == 0:
            print("Fizz!")
        elif num % 5 == 0:
            print("Buzz!")
        else:
            print(num)

def fizzbuzz_while(times):
    counter = 1
    while times >= counter:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz!!")
        elif counter % 3 == 0:
            print("Fizz!")
        elif counter % 5 == 0:
            print("Buzz!")
        else:
            print(counter)
        counter +=1

fizzbuzz_for(100)
fizzbuzz_while(100)
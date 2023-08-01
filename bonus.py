def fizzbuzz_for():
    for i in range(1 , 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
          print("FizzBuzz")
        else:
           print(i) 

print("fizzbuzz by For loop : ")
fizzbuzz_for()
print("-"*30)

def fizzbuzz_while():
    number =1 
    while number!=101:
        if number%3==0 and number%5==0:
            print("FizzBuzz")
        elif number%3==0:
            print("Fizz")
        elif number%5==0:
            print('Buzz')
        else :
            print(number)
        number+=1

print("fizzbuzz by While loop :")
fizzbuzz_while()
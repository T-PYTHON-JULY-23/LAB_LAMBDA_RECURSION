
multi_3_lambda = lambda number : number%3==0
multi_5_lambda=lambda number: number%5==0
multi_5_3_lambda=lambda number:number%5==0 and number%3==0

print("FizzBuzz in for loop")
#FizzBuzz in for loop 
for number in range(1,100):
    if multi_3_lambda(number):
        print("Fizz")
    elif multi_5_lambda(number):
        print("Buzz")
    elif multi_5_3_lambda(number):
        print("FizzBuzz") 
    else:
        print(number)

#FizzBuzz in while loop
print("FizzBuzz in while loop")
number=0
end=100
counter=0
while number<end:
    number+=1
    if multi_3_lambda(number):
        print("Fizz")
    elif multi_5_lambda(number):
        print("Buzz")
    elif multi_5_3_lambda(number):
        print("FizzBuzz") 
    else:
        print(number)

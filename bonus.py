
def Fizz_Buzz_ForLoop():

    for val in range(1,100):
        
        if val%3 == 0:
            print("Fizz")
        elif val%5 == 0:
            print("Buzz")
        elif val%15 == 0:
            print("FizzBuzz")
        else:
            print(val)
        if val ==100:
            break


def Fizz_Buzz_WhileLoop() :
    n= 1
    while n <=100:
        if n%3 == 0:
            print("Fizz")
            n+=1
        elif n%5 == 0:
            print("Buzz")
            n+=1
        elif n%15 == 0:
            print("FizzBuzz")
            n+=1
        else:
            print(n)
            n+=1
        if n ==100:
            break



print("-"*20)
print("the answer using foor loop")
print("-"*20)
print(Fizz_Buzz_ForLoop())


print("-"*20)
print("the answer using while loop")
print("-"*20)
print(Fizz_Buzz_WhileLoop())
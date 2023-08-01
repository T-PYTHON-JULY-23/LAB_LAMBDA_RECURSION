print("-"*30)
print("      Using for loop       ")
print("-"*30)
for i in range(1,100+1):
    if i%3 == 0:
        print("Fizz",i)
    if i%5 == 0:
        print("Buzz",i)
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz",i)


print("-"*30)
print("      Using while loop       ")
print("-"*30)

def fun1():
    i=1
    while i in range(1,100+1):
        i+=1
        if i%3 == 0:
            print("Fizz",i)
        if i%5 == 0:
            print("Buzz",i)
        if i%5 == 0 and i%3 == 0:
            print("FizzBuzz",i)

fun1()
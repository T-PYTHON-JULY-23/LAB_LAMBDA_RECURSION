# Bonus (solve in a new file)
# Exercise: FizzBuzz

# FizzBuzz is a common coding problem that asks you to print the numbers from 1 to 100. However, there are a couple of exceptions:

# For multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz" instead of the number.
# For numbers which are multiples of both three and five, print "FizzBuzz".
# Try to write a Python program that accomplishes this task using a function with a "for" loop. After you've completed that, try to write the same program but using a "while" loop instead.

# Remember to test your code to ensure it's working as expected!

# Hints:

# You can use the modulus operator % to check if a number is a multiple of another number. For example, n % 3 == 0 checks if n is a multiple of 3.
# For the "for" loop, consider using the range function.
# For the "while" loop, you'll need to manually increment your counter

def FizzBuzz():
 for i in range(1,100+1):
  if i % 3 == 0 and  i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
FizzBuzz()



print("----"*15)



def fizzbuzz():
  S = 1
  while S <= 100:
    if S % 3 == 0 and  S % 5 == 0:
          print("FizzBuzz")
    elif S % 3 == 0:
        print("Fizz")
    elif S % 5 == 0:
        print("Buzz")
    else:
        print(S)
    S+=1
fizzbuzz()
           
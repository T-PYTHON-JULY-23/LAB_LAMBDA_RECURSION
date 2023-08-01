'''
1. For multiples of three, print "Fizz" instead of the number.
2. For multiples of five, print "Buzz" instead of the number.
3. For numbers which are multiples of both three and five, print "FizzBuzz".
'''
for n in range(1,101):
    if n % 3 ==0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 ==0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
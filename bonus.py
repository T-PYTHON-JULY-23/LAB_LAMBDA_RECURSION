print("-"*15)
print("Using for loop")
print("-"*15)

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i,)
print("-"*16)
print("Using while loop")
print("-"*16)

counter =1
while counter < 101:
    
 if counter%3==0 and counter%5==0:
        print("FizzBuzz")
 elif counter%3==0:
        print("fizz")
 elif counter%5==0:
        print("Buzz")

 else:
        print(counter)
 counter +=1 

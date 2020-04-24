print("Hello, welcome to the FizzBuzz game ;)")
number = int(input("Select a number betwen 1 and 100: "))

for number in range(1, number+1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

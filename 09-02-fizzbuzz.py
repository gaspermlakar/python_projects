print("Hello, welcome to the FizzBuzz game ;)")
upper_count_limit = int(input("Select a number betwen 1 and 100: "))

for current_count in range(1, upper_count_limit+1):
    if current_count % 3 == 0 and current_count % 5 == 0:
        print("fizzbuzz")
    elif current_count % 3 == 0:
        print("fizz")
    elif current_count % 5 == 0:
        print("buzz")
    else:
        print(current_count)

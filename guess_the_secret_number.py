SECRET = 8

guess = int(input("What is my secret number? (between 1 and 20) "))

if guess == SECRET:
    print("YEEEEEEE, you find my number!")
else:
    print("Wrong, choose another number... The secret number is not " + str(guess))

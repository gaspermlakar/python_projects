import random

secret = random.randint(1,30)
attempts = 0

with open("08-02-score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score: " + str(best_score))

while True:
    guess = int(input("What is my secret number? (between 1 and 30) "))
    attempts += 1

    if guess == secret:
        if attempts < best_score:
            with open("08-02-score.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("YEEEEEEE, you guessed it! It's number " + str(secret))
        print("Attempts nedded: " + str(attempts))
        break

    if guess > secret:
         print("Your guess is wrong... try something smaller ")

    elif guess < secret:
        print("Your guess is wrong... try something bigger ")
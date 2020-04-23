import random


secret = random.randint(1, 30)
attempts = 0
with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("How low can you go? Top Score is currently: " + str(best_score))


while True:
    guess = int(input("Number_nine_Loops_and_conditions (between 1 and 30): "))
    attempts += 1
    if guess == secret:
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("You've guessed it - congratulations! It's number " + str(secret))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


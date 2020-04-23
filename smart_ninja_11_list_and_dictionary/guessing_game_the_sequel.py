# import json
# import random
# import datetime
#
# current_time = datetime.datetime.now()
#
# print(current_time)
#
# score_data = {"attempts": attempts, "date": datetime.datetime.now()}
#
# [{"attempts": 6, "date": "2019-03-01 12:30:56.198449"}, {"attempts": 5, "date": "2019-03-03 18:26:19.439882"}, {"attempts": 6, "date": "2019-03-18 09:55:01.734739}]
#
# secret = random.randint(1, 30)
# attempts = 0
#
# with open("score_list.txt", "r") as score_file:
#     score_list = json.loads(score_file.read())
#     print("Top score: " + str(score_list))
#
# for score_dict in score_list:
#     print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
#
# while True:
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#     attempts += 1
#
#     if guess == secret:
#         score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
#
#         with open("score_list.txt", "w") as score_file:
#             score_file.write(json.dumps(score_list))
#
#         print("You've guessed it - congratulations! It's number " + str(secret))
#         print("Attempts needed: " + str(attempts))
#         break
#     elif guess > secret:
#         print("Your guess is not correct... try something smaller")
#     elif guess < secret:
#         print("Your guess is not correct... try something bigger")
#
#

import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
# a user can enter data (via input()) and at the end of the program,
# the data gets saved in a text file.

print("Enter some football player's data!")

f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height = input("Enter player's height: ")
weight = input("Enter player's weight: ")
goals = input("Enter the number of player's goals: ")
y_cards = input("Enter the number of player's yellow cards: ")
r_cards = input("Enter the number of player's red cards: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

with open("football_players.txt", "w") as football_file:
    football_file.write(str(new_player.__dict__))

print("Player successfully entered!")
print("player's data: {0}".format(new_player.__dict__))
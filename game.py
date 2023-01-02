import random


def change_player(player):
    if player == "Jack":
        return "John"
    else:
        return "Jack"


def robot_taking(pencils):
    if pencils <= 2 or pencils % 4 == 2:
        return 1
    elif pencils == 3 or pencils % 4 == 3:
        return 2
    elif pencils % 4 == 0:
        return 3
    else:
        return random.randint(1, 3)


print("How many pencils would you like to use:")

pencils_number = 0
while pencils_number == 0:
    pencils_input = input()
    if not pencils_input.isdigit():
        print("The number of pencils should be numeric")
    else:
        if int(pencils_input) == 0:
            print("The number of pencils should be positive")
        else:
            pencils_number = int(pencils_input)

print("Who will be the first (John, Jack):")
current_player = input()
while current_player != "John" and current_player != "Jack":
    print("Choose between 'John' and 'Jack'")
    current_player = input()


while pencils_number > 0:
    print("|" * pencils_number)
    current_number = 0
    if current_player == "John":
        print("John's turn!")
        turn = False
        while not turn:
            current_input = input()
            if current_input not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            elif int(current_input) > pencils_number:
                print("Too many pencils were taken")
            else:
                current_number = int(current_input)
                turn = True
    else:
        print("Jack's turn:")
        current_number = robot_taking(pencils_number)
        print(current_number)
    pencils_number = pencils_number - current_number
    current_player = change_player(current_player)

print(current_player + " won!")


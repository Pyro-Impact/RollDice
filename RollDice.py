from Shift15.Restart_Function import confirm_restart
import random


def roll(number_rolled):
    num_list = [1, 2, 3, 4, 5, 6]
    a = ""
    for i in range(1, number_rolled + 1):
        a += "[" + str(random.choice(num_list)) + "],"
    return a


while True:
    while True:
        try:
            user_input = int(input("Please enter the number of times you want to roll the die: "))
            break
        except ValueError:
            print("Please try again.")

    print(roll(user_input)[:-1])
    if confirm_restart() == "yes":
        continue
    else:
        break

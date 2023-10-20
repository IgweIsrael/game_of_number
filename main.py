import random
print("Welcome to number of chance that lead to luck")
best_luck_no = input("Do you want to play the game of lucky number! then type any number! ")
print(best_luck_no)
if best_luck_no.isdigit():
    best_luck_no = int(best_luck_no)

    if best_luck_no <= 0:
        print("Type positive number greater than 0 for better luck next time")
        quit()
else:
    print("Type number that can increase your chance of luck next time ")
    quit()

random_number = random.randint(0, best_luck_no)
guess = 0

while True:
    guess += 1
    personal_guess = input("Try your guess? ")
    if personal_guess.isdigit():
        personal_guess = int(personal_guess)

    else:
        print("Type a number that can increase your chance of luck next time")
        continue

    if best_luck_no == personal_guess:
        print("You make the right choice")
        break

    elif best_luck_no > personal_guess:
        print("You are above the required number choice")
    else:
        print("You are below the required number choice")

print(f"You have try your best but after {guess} chances before you are lucky")
print("Thank you for attempting this game")

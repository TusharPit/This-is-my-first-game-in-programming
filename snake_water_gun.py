# Tushar Patil Productions tp,inc

import random
print("Welcome to Snake, Water, Gun game")
print("Press s for Snake")
print("Press w for Water")
print("Press g for gun \n")
total_chance = 5
current_chance = 0
computer_point = 0
human_point = 0
lst = ['s','g','w']
x = current_chance < total_chance
while(current_chance <= total_chance):
    human_choice = input("Enter s,w or g :")
    computer_choice = random.choice(lst)
    if human_choice == 'g' and computer_choice == 'w':
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("Computer got 1 point and you got 0 point")
        human_point = human_point + 1

    elif human_choice == 'w' and computer_choice == 'g':
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("You got 1 point and computer got 0 point")
        human_point = human_point + 1

    elif human_choice == 's' and computer_choice == 'w':
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("You got 1 point and computer got 0 point")
        human_point = human_point + 1

    elif human_choice == 'w' and computer_choice == 's':
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("Computer got 1 point and you got 0 point ")
        computer_point = computer_point + 1

    elif human_choice == 'g' and computer_choice == 's':
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("You got 1 point and computer got 0 point ")
        human_point = human_point + 1

    elif human_choice == 's' and computer_choice == 'g':
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("Computer got 1 point and you got 0 point")
        computer_point = computer_point + 1

    elif human_choice == computer_choice:
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("Computer and you got 0 points")
        computer_point = computer_point + 0
        human_point = human_point + 0
    else:
        print(f"Your choice was {human_choice} and computer's choice was {computer_choice}")
        print("Operation not defined ", computer_choice)
        print("somethingg went wrong")
    current_chance+=1
print("Game Over")

print(f" your points are {human_point} and Computer points are {computer_point}")
if(human_point>computer_point):
    print("You Won")

elif computer_point > human_point:
    print("Computer Won")
elif computer_point==human_point:
    print("Match is tie")






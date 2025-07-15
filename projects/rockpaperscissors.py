import random

user_win = 0
computer_win = 0

choices = {
    0 : "rock",
    1 : "paper",
    2 : "scisseros"
}
print(" 0 : 'rock' \n 1 : 'paper' \n 2 : 'scisseros'")


while True:
    user_input = input("Enter your choices: ")
    computer_choice = random.randint(0, 2)
    user_choice = int(user_input)

    print(f"computer choice : {choices[computer_choice]}")
    print(f"your choice : {choices[user_choice]}")

    if computer_choice == 0 and user_choice == 1 :
        print ("You win")
        user_win += 1
    elif computer_choice == 1 and user_choice == 2 :
        print("You win")    
        user_win += 1
    elif computer_choice == 2 and user_choice == 0 :
        print("You win")    
        user_win += 1
    elif computer_choice == user_choice :
        print("Game Draw")    
    else :
        print("I win")
        computer_win += 1

    another_game = input("quit: yes(y) ?")
    print('\n')
    if another_game.lower() == "y":
        break

print(f"your score is {user_win}")    
print(f"computer's score is {computer_win}")


print("Thank you for playing ❤️")
print('\n')
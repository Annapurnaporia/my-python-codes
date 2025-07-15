import random

top_range = input("Enter a number: ")

if top_range.isdigit() :
    top_range = int(top_range)
    if top_range <= 0 :
        print("Please type a number a number greater than 0 next time.")
        quit()
else :
    print("Please enter a number.")
    quit()    

random_number = random.randint(0, top_range)        
guess = 0


while True:
    guess += 1
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("please enter a number.") 
        continue   

    if user_guess == random_number:
        print("you got it!🎉") 
        break

    elif user_guess < random_number:
        print("you are below the number!")     

    else:
        print("you are above the number!")      

print(f"you got it in {guess} guesses")

print(f"the number was {random_number}")

print("Thanks for playing! ❤️")
print("Welcome to the Quiz Game!")

score = 0
playing_game = input("do yiu want to paly ? (yes/No)")
if playing_game.lower() == "yes" :
    print("Great ! Let's start the game. 😃 ")

else:
    print("okay bye! 👋")
    quit()

Question_one = input("Q1:  what is the fullform of CPU ? ")
answer_one = "central processing unit"
if Question_one.lower() == answer_one.lower() :
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! 😥", "\n" "The correct answer is central processing unit ")

Question_two = input("Q2:  what is the fullform of RAM ? ")
answer_two = "random access memory"
if Question_two.lower() == answer_two.lower() :
    print("Correct! 🎉")
    score += 1

else:
    print("Wrong! 😥", "\n" "The correct answer is random access memory")

Question_three = input("Q3:  what is the fullform of ROM ? ")
answer_three = "read only memory"
if Question_three.lower() == answer_three.lower() :
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! 😥", "\n" "The correct answer is read only memory")

Question_four = input("Q4:  what is the fullform of CD ? ")
answer_four = "compact disc"
if Question_four.lower() == answer_four.lower() :
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! 😥", "\n" "The correct answer is compact disc")

Question_five = input("Q5:  what is the fullform of DVD ? ")
answer_five = "digital versatile disc"
if Question_five.lower() == answer_five.lower() :
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! 😥", "\n" "The correct answer is digital versatile disc ")


if Question_one.lower() == answer_one.lower() and Question_two.lower() == answer_two.lower() and Question_three.lower() == answer_three.lower() and Question_four.lower() == answer_four.lower() and Question_five.lower() == answer_five.lower() :
    print("CONGRATULATIONS ! 🏆")
    print("You have successfully completed the quiz.")
else :
    print(f"your score is {str(score)} out of 5")
    print(f"you have got {str((score/5)*100)}%") 


print("Thanks for playing the Quiz Game! ❤️❤️")       


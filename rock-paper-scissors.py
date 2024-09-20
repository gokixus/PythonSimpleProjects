import random

user_score = 0
computer_score = 0

while True:
    print("\n1-Rock\n2-Paper\n3-Scissors")
    user_choice = input("Your shoice: ")
    computer_choice = random.choice(["1", "2", "3"])
    
    if user_choice == "1": #islemler
        if computer_choice == "1":
            print("Computer is shoice: Rock. Scoreless!")
        elif computer_choice == "2":
            print("Computer is shoice: Paper. You lose!")
            computer_score += 100
        elif computer_choice == "3":
            print("Computer is shoice: Scissors. You Win!")
            user_score += 100
    elif user_choice == "2":
        if computer_choice == "1":
            print("Computer is shoice: Rock. You win!")
            user_score += 100
        elif computer_choice == "2":
            print("Computer is shoice: Paper. Scroeless!")
        elif computer_choice == "3":
            print("Computer is shoice: Scissors. You lose!")
            computer_score += 100
    elif user_choice == "3":
        if computer_choice == "1":
            print("Computer is shoice: Rock. You lose!")
            computer_score += 100
        elif computer_choice == "2":
            print("Computer is shoice: Paper. You win!")
            user_score += 100
        elif computer_choice == "3":
            print("Computer is shoice: Scissors. Scoreless!")
    else:
        break

print(f"\nUser is score: {user_score}\nComputer is score: {computer_score}")
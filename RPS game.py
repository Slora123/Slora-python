import random
list=["rock","paper","scissor"]
comp_point=0
user_point=0
while comp_point<10 and user_point<10:
    computer_choice=random.choice(list)
    user_choice=input("rock/paper/scissor?:-")
    if user_choice in list:
        print("Computer's choice:",computer_choice)
        if user_choice==computer_choice:
            print("It's a Tie")
        elif (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissor" and computer_choice=="paper") or (user_choice=="rock" and computer_choice=="scissor"):
            user_point+=1
            print("You Win this Round!")
            print("Your Score:",user_point)
            print("Computer's score:",comp_point)
        else:
            comp_point+=1
            print("You Lose this Round :( ")
            print("Your Score:",user_point)
            print("Computer's score:",comp_point)
    else:
        print("Invalid choice...")
if comp_point==10:
    print("You Win!")
else:
    print("You Lose")

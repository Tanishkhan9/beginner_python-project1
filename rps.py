import random
score=0
operations=["rock" , "paper" ,"scissors"]
while True:
    
    user_input=input("please ,type your input rock/paper/scissors or quit: ").lower()
    if user_input=="quit":
        print("your score:",score)
        break
    elif user_input not in operations:
       continue
    computer_choice = random.choice(operations)
    print("let the computer choose:")
    print("the computer choose :",computer_choice)
    if user_input==computer_choice:
        print("this is a tie")
    elif (user_input == "rock" and computer_choice == "scissors") or \
        (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("you won!")
        score += 1
        print("yous score is :",score)
    else:    
        print("you lost!")
        print("your score is:",score)
 
import random
r=random.randint(0,50)


top_of_range=input("enter a number= ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
else:
    print("please enter a valid number")
    quit()
if top_of_range <=0:
    print("please enter a positive number")
    quit()

    

random_number = random.randint(0, top_of_range)
while True:

    user_guess = input("make a guess: ")

    if user_guess.isdigit():    
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue 

    if user_guess == random_number:
        print('congratulation, you got correct.')
        break

    else:
        print("you guess a wrong number")

    



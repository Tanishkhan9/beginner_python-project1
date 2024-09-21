print("hello")
playing = input("do you wanna play a quiz? ")
if playing!="yes":
    print("okay, see you later")
    quit()
print("okay , lets play the quiz.")
score=0
answer=input("whats is the full form of cpu? ")
if answer.lower()=="central processing unit":
    print("correct answer!")
    score+=1
else:
     print("wrong answer!")
answer=input("whats is the full form of gpu? ")
if answer.lower()=="graphic processing unit":
    print("correct answer!")
    score+=1
else:
    print("wrong answer!")
answer=input("whats is the full form of psu? ")
if answer.lower()=="power supply unit":
    score+=1
    print("correct answer!")
else:
    print("wrong answer!")
answer=input("whats is the full form of cu? ")
if answer.lower()=="control unit":
    score+=1
    print("correct answer!")
else:
    print("wrong answer!")
answer=input("whats is the full form of alu? ")
if answer.lower()=="algorithm and logical unit":
    score+=1
    print("correct answer!")
else:
    print("wrong answer!")

print(score)
print((score/5)*100)
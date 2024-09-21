master_pwd=input("please enter your password:")
question=input("what would you like to do ? :add new password or view existing one's  !--(add|view)")

def add():
    name = input("Enter account name: ")
    pwd = input("enter new password: ")
    with open('password.txt','a') as f:
        f.write(name+ " |" + pwd +"\n")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            print(line)  

while True:

    if question=="add":
        add()
        break
    if question=="view":
        with open("password.txt",'r') as f:
         view()
        break
    else:
         print("wrong input!")
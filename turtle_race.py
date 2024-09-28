import turtle
import random
import time
WIDTH, HEIGHT=800,800
COLORS=['red','black','cyan','blue','green','grey','brown','yellow','pink','orange']





def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("khansahab racing hub:")
    
def create_turtles(colors):
    turtles=[]
    spacingx= WIDTH // (len(colors) +1)
 
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.pendown()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2+20)
        turtles.append(racer)
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup() 
        racer.forward(100)
        racer.speed(1)
        racer.forward(200)
        racer.speed(0)
     
    return turtles
        

def get_no_of_racers():
    while True:
        racers=input("enter the number of turtles you wan to race ( 2 - 10 ): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Invalid input. Please enter a number.")
            continue
        if  2 <= racers <=10 :
            return racers
        else:   
            print( "number of racers should be in between 2-10! ")
    

racers_count = get_no_of_racers()
init_turtle()
random.shuffle(COLORS)
color=COLORS[:racers_count]

turtles=create_turtles(color)



turtle.done()
def average(x):
    avg=x/5
    return avg

def main():

    player1=input("what is player1's last name:")
    print()
    jersey1=int(input("what is their jersey number:"))
    print()
    while ((1>=jersey1)or(jersey1>99)):
        jersey1=int(input("re-enter the jersey number in range 1-99:"))

    yard1=float(input("How many yards did you run in your first game:"))
    for i in range(4):
        yards=float(input("How many yards did you run in your next game:"))
        yard1=yard1+yards
        avg=average(yard1)
    print("your total yards were",yard1)
    print("You averaged",avg,"yards")
#list=[0,0,0,0,0]
#for in range(0,5):
#list1[i]=float(input("enter the yards in game"))
    print()
    print()


    player2=input("what is player2's last name:")
    print()
    jersey2=int(input("what is their jersey number:"))
    print()
    while ((1>=jersey2)or(jersey2>99)):
        jersey2=int(input("re-enter the jersey number in range 1-99:"))

    yard2=float(input("How many yards did you run in your first game:"))
    for i in range(4):
        yards2=float(input("How many yards did you run in your next game:"))
        yard2=yard2+yards2
        avg2=average(yard2)
    print("your total yards were",yard2)
    print("You averaged",avg2,"yards")
    print()

    print("Player number",jersey1,player1,"average yards per game was:",avg)
    print("Player number",jersey2,player2,"average yards per game was:",avg2)
    print()
    if avg>avg2:
        print(player1," is the better draft pick")
    else:
        print(player2,"is the better draft pick")



main()
    #player2=input("what is your last name:")
    #print()

    #jersey2=input(int("what is your jersey number:"))
    #print()

    #while 0<jersey2<=99:
    #    yard1=input(float("How many yards did you run in your first game:"))
    #    for i in range(4):
    #        yards=input(float("How many yards did you run in your second game:"))
    #        yard1=yard1+yards
        #else:
        #    input(int("Re-enter a jersey number within the range 1-99:"))

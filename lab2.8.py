def main():
    print ("This function calculates the sum of any series of numbers")
    y=0
    x=int(input("How many numbers are you adding:"))
    for i in range(0,x):
        x=int(input("Enter number:"))
        y=y+x
    print(y)

main()

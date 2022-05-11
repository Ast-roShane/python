def main():
    import math
    print("This program will calculate the standard deviation of any given numbers")
    x=(int(input("Please enter how many numbers you'd like to calculate the standard deviation of:")))
    sum=0
    w=0
    for i in range(x):
        meannum=(float(input("enter number:")))
        sum= sum+meannum
        print()
        mean= sum/x
        y=((meannum-mean)**2)
        w=w+y
    SD= math.sqrt(w/(x-1))
    print("The mean is:",mean)
    print()
    print("You standard deviation is:",round(SD,2))


main()

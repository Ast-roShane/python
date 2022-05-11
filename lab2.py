def main():
    print("This function computes the factorial of any given number")
    x= eval(input("Enter a number:"))
    for i in range(1,x):
        x=x*i
    print(x)
main()

def main():
    print("This function will calculate any amount in different forms")
    amt = (eval(input("Enter the cash value:")))
    dollar=((amt*100)//100)
    amt1=(amt-dollar)
    quarters=(amt1//.25)
    amt1 = (amt1%.25)
    dime = (amt1//.1)
    amt1= (amt1%.1)
    nickle = (amt1//.05)
    amt1 = (amt1%.05)
    pennies = (amt1//.01)

    print("you have",dollar,"dollars\n","you have", quarters,"quarters\n","you have",dime,"dimes \n","you have",nickle,"nickles \n","you have",pennies,"pennies \n")
main()

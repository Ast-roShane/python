def main():
    print ("This function calculates your average and gives you a letter grade")
    x=int(input("How many classes are you taking:"))
    grade1=(int(input("what did you recieve in your first class:")))
    for i in range(x-1):
        grade=(int(input("What grade did you recieve for your next class:")))
        grade1=grade1+grade
    mean= grade1/x
    print(mean)
    paper=input("did you complete the paper(yes/no):")
    if paper[0]=="yes":
        if mean>=90:
            Print(mean,"You have an A")
        elif (90>mean>=80):
            print(mean,"you have a B")
        elif(80>mean>=70):
            print(mean,"you have a C")
        elif(70>mean>=65):
            print(mean,"you have a D")
        else:
            print(mean,"you failed")
    else:
        print("you failed the class")
main()

def time(x):
    runner1=int(x.split(":")[0])
    runner2=int(x.split(":")[1])
    minutes_seconds=(runner1*60)+runner2
    return minutes_seconds



def main():
    time1=input("Enter the time for runner1 in the form mm:ss:")
    print()
    time2=input("Enter the time for runner2 in the form mm:ss:")
    print()
    runner1=time(time1)
    runner2=time(time2)
    if runner1<runner2:
        print("runner 1 is the winner")
        print()
        ("Train more like Tim next time runner 2.")
    elif runner1>runner2:
        print("runner 2 is the winner")
        print()
        print("Train more like Tim next time runner 1")
    elif runner1==runner2:
        print("Its a tie")
main()

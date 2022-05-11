


def SumN(m):
    sum=0
    for i in range(1,m+1):
        sum=i+sum
    return sum
def sumCubeN(m):
    cube=0
    for i in range(1,m+1):
        cube=(i**3)+cube
    return cube

def main():
    n=int(input("Enter a number:"))
    x=SumN(n)
    y=sumCubeN(n)
    print(x,y)

main()

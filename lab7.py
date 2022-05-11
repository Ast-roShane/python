def circ(x):
    import math
    circumfrence=2*math.pi*x
    return circumfrence
def area(y):
    import math
    area=math.pi*y**2
    return area
def main():
    import math

    print("This function calculates the circumfrence and area with just the radius")
    Rad=float(input("What is your radius:"))
    x=circ(Rad)
    y=area(Rad)
    print("Your cicumfrence is",round(x,2),"Your area is",round(y,2))
main()

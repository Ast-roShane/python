def main():
    print(" this function will compute the lenght of a ladded required to reach a given height when leaned against a house")
    import math

    height=float(input("what is the height of the house?:"))
    angle=float(input("what is the angle for the house?:"))

    radians=(math.pi/180)*angle
    length=(height)/math.sin(radians)
    length=round(length,2)
    print(length)
main()

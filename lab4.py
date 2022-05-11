def main():
    print("this function creates acronyms of any given phrase")
    x=input("enter a phrase:")
    y=x.split()
    w=""
    for i in range(len(x.split())):
        w= w+x.split()[i][0]
    print(w.upper())
main()

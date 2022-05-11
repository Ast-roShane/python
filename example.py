def main():
    firstentry=input("what is the your class:")
    unicode=ord(firstentry[1])

    uinteger=ord(firstentry[0])

    while ((0<=uinteger)or(uinteger<8) and (65<=unicode)or(unicode<=90)):
        firstentry=input("what is the your class:")
main()

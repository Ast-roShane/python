def main():
    print("This function encodes")
    key=int(input("enter your cipher key:"))
    inString = input("Please enter the Unicode-encoded message: ")
    message=""
    for ch in inString:
        num= ord(ch)
        num1=num+key
        message= message+chr(num1)
    print("your coded message is",message)
    decoder=""
    for ch in message:
        x= ord(ch)
        key1= x-key
        decoder= decoder+chr(key1)
    print("your decoded message is:",decoder)

main()

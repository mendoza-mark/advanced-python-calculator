running = True

while running:
    n1 = float(input("Please Enter your First Number: "))
    op = input("Enter your Desired Operation (+, -, /, *, **, %, //): ")
    n2 = float(input("Please Enter your Second Number: "))

    if op == "+":
        print ("Answer:", n1 + n2)

    elif op == "-":
        print ("Answer:",n1 - n2)

    elif op == "/":
        if n2 == 0:
            print ("Invalid, cannot divide by 0")
        else:
            print ("Answer:",n1 / n2)

    elif op == "*":
        print ("Answer:", n1 * n2)

    elif op == "**":
        print ("Answer:", n1 ** n2)

    elif op == "%":
        print ("Answer:", n1 % n2)

    elif op == "//":
        if n2 == 0:
            print ("Invalid, cannot divide by 0")
        else:
            print ("Answer:", n1 // n2)

    else:
        print ("Invalid.")

    again = input("Do you want to calculate again? (Y/N): ")

    if again == "N":
        print ("Thank you.")
        running = False 
    elif again == "Y":
        running = True
    else:
        print ("Invalid.")
        running = False

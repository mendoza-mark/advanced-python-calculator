import math

running = True

while running:
    print("\n--- Calculator ---")
    print("Basic: +  -  *  /  **  %  //")
    print("Advanced: sqrt  log  ln  sin  cos  tan  fact")
    print("Other: abs  round  max  min")
    
    op = input("Enter operation: ").lower()

    if op in ["+", "-", "*", "/", "**", "%", "//", "max", "min"]:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            if n2 == 0:
                print("Invalid, cannot divide by 0")
                result = None
            else:
                result = n1 / n2
        elif op == "**":
            result = n1 ** n2
        elif op == "%":
            result = n1 % n2
        elif op == "//":
            if n2 == 0:
                print("Invalid, cannot divide by 0")
                result = None
            else:
                result = n1 // n2
        elif op == "max":
            result = max(n1, n2)
        elif op == "min":
            result = min(n1, n2)

    elif op in ["sqrt", "log", "ln", "sin", "cos", "tan", "fact", "abs", "round"]:
        n = float(input("Enter number: "))

        if op == "sqrt":
            if n < 0:
                print("Invalid input")
                result = None
            else:
                result = math.sqrt(n)
        elif op == "log":
            if n <= 0:
                print("Invalid input")
                result = None
            else:
                result = math.log10(n)
        elif op == "ln":
            if n <= 0:
                print("Invalid input")
                result = None
            else:
                result = math.log(n)
        elif op == "sin":
            result = math.sin(math.radians(n))
        elif op == "cos":
            result = math.cos(math.radians(n))
        elif op == "tan":
            result = math.tan(math.radians(n))
        elif op == "fact":
            if n < 0 or not n.is_integer():
                print("Invalid input")
                result = None
            else:
                result = math.factorial(int(n))
        elif op == "abs":
            result = abs(n)
        elif op == "round":
            d = int(input("Decimal places: "))
            result = round(n, d)

    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print("Answer:", result)

    again = input("Do you want to calculate again? (Y/N): ").upper()

    if again == "N":
        print("Thank you.")
        running = False
    elif again == "Y":
        running = True
    else:
        print("Invalid.")
        running = False

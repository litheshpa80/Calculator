import art
def add(n1, n2):
   return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
calc = {"+": add, "-": subtract, "*": multiply, "/": divide}
while True:
    print(art.logo)
    should_accumulate = True
    num1 = int(input("Enet the first number: "))
    while should_accumulate:
        for c in calc:
            print(c)
        sym = input("Pick a symbol: ")
        num2 = int(input("Eneter the second number:"))
        result = calc[sym](num1, num2)
        print(f"{num1} {sym} {num2} = {result}")
        choice = input("type y to continue or n to exit:")
        if choice == "y":
            num1 = result
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            break
    continue






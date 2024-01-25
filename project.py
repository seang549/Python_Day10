from art import logo
print(logo)


# Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = { "+": add,
               "-": subtract,
               "*": multiply,
               "/": divide }

def calculate():

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number?: "))
    function = operations[operation_symbol]
    answer = function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_calculating = True
    while continue_calculating:
        repeat = input(f"Type 'y' to continue calculating with {answer}, type 'new' to start a new calculation, or 'n' to exit.: ").lower()
        if repeat == 'n':
            continue_calculating = False
            print('Goodbye')
            return
        elif repeat == 'new':
            continue_calculating = calculate()
        elif repeat == 'y':
            num1 = answer
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation from the line above: ")

            num2 = float(input("What's the second number?: "))
            function = operations[operation_symbol]
            answer = function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("That was not a choice.\n Goodbye")
            continue_calculating = False
            return

calculate()

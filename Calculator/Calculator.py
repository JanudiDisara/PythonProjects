import art
# We cannot assign a function with brackets to a variable
# answer = add(1, 2)
# print(answer)

# Instead do this:
# answer = add
# print(answer(1, 2))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

continue_working = 'y'

calc_dictionary = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: Division by zero"
}

print(art.logo)

while True:  # Infinite loop to restart the calculation when needed
    n1 = int(input("What's the first number? "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = int(input("What's the next number? "))

    result = calc_dictionary[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")

    while True:  # Loop to continue calculations with the result
        continue_working = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if continue_working == 'n':
            print("\n" * 30)
            break  # Break out of inner loop, restarting the main loop

        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        n2 = int(input("What's the next number? "))

        result2 = result
        result = calc_dictionary[operation](result, n2)
        print(f"{result2} {operation} {n2} = {result}")
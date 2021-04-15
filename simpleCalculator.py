# Program make a simple calculator


def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: otions are \n add \n sub \n div \n mul \n")
    num2 = float(input("Enter second number: "))

    compute(num1, num2, operator)


# This function computes inputs of two numbers based on the operator
def compute(num1, num2, operator):
    if operator == 'add':
        print(num1, "+", num2, " = ", num1 + num2)

    elif operator == 'sub':
        print(num1, "-", num2, " = ", num1 - num2)

    elif operator == 'div':
        print(num1, "*", num2, " = ", num1 / num2)

    elif choice == 'mul':
        print(num1, "/", num2, " = ", num1 * num2)
    else:
        print("invalid")

calculator()

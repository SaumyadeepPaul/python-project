print("Welcome to the Calculator!")

num1 = float(input("Please enter a number: "))

op = input("Please Enter a operator: ")

num2  = float(input("Please enter another number: "))


def calc(op):
    if op == "+":
        print(f"{num1} plus {num2} is equal to {num1 + num2}")

calc(op)

def calc(op):
    if op == "-":
        print(f"{num1} minus {num2} is equal to {num1 - num2}")

calc(op)

def calc(op):
    if op == "*":
        print(f"{num1} multiply by {num2} is equal to {num1 * num2}")

calc(op)

def calc(op):
    if op == "/":
        print(f"{num1} divided by {num2} is equal to {num1 / num2}")

calc(op)

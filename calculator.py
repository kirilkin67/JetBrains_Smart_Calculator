# write your code here
from collections import deque

PLUS = "+"
MINUS = "-"
ERROR_EXPRESSION = "Invalid expression"
ERROR_IDENTIFIER = "Invalid identifier"
ERROR_ASSIGNMENT = "Invalid assignment"
ERROR_VARIABLE = "Unknown variable"
HELP = """The program calculates:
-addition of numbers
-subtraction of numbers
-multiply of numbers
-division of numbers
-close program -> '/exit'"""


def is_number(number):
    if (number[0] == MINUS or number[0] == PLUS) and number[1:].isdigit():
        return True
    return number.isdigit()


def is_brackets(string):
    brackets = deque()
    for char in string:
        if char == "(":
            brackets.append(char)
        if char == ")":
            if len(brackets) == 0 or brackets.pop() != "(":
                return False
    return True if len(brackets) == 0 else False


def variables_validation(user_input, variables):
    if user_input.count("=") == 1:
        key, value = user_input.replace(" ", "").split("=")
        if key.isalpha() and is_number(value):
            variables[key] = value
        elif key.isalpha() and value.isalpha():
            if value in variables.keys():
                variables[key] = variables[value]
            else:
                print(ERROR_VARIABLE)
        elif not key.isalpha():
            print(ERROR_IDENTIFIER)
        elif not is_number(value) or not value.isalpha():
            print(ERROR_ASSIGNMENT)
    else:
        print(ERROR_ASSIGNMENT)


def operator_type(operator):
    if operator[0] == PLUS:
        return PLUS
    elif operator[0] == MINUS:
        return PLUS if len(operator) % 2 == 0 else MINUS
    return operator


def is_operator(operator):
    if operator.startswith((PLUS, MINUS)):
        if operator.count(PLUS) == len(operator) or \
                operator.count(MINUS) == len(operator):
            return True
    if operator.startswith(("*", "/")) and len(operator) == 1:
        return True
    return False


def infix_to_postfix(user_input):
    operator = deque()
    postfix = list()
    for token in user_input:
        if is_number(token):
            postfix.append(token)
        elif token == "(":
            operator.append(token)
        elif token == ")":
            while operator[-1] != "(":
                postfix.append(operator.pop())
            operator.pop()
        elif is_operator(token):
            if len(operator) == 0 or operator[-1] == "(":
                operator.append(operator_type(token))
            elif (token == "*" or token == "/") and (operator[-1] == PLUS or operator[-1] == MINUS):
                operator.append(operator_type(token))
            else:
                while operator and operator[-1] != "(":
                    postfix.append(operator.pop())
                operator.append(operator_type(token))
    while operator:
        postfix.append(operator.pop())
    return postfix


def smart_calculator(numbers):
    calculator = deque()
    result = 0
    for elem in numbers:
        if is_number(elem):
            calculator.append(elem)
        elif is_operator(elem):
            num_1 = int(calculator.pop())
            num_2 = int(calculator.pop())
            if elem == PLUS:
                result = num_2 + num_1
            if elem == MINUS:
                result = num_2 - num_1
            if elem == "*":
                result = num_2 * num_1
            if elem == "/":
                if num_1 == 0:
                    return ERROR_EXPRESSION
                result = num_2 / num_1
            calculator.append(result)

    return int(calculator.pop()) if len(calculator) == 1 else ERROR_EXPRESSION


def main():
    variables = dict()
    while True:
        user_input = input().strip()
        if not user_input:
            continue
        elif user_input.startswith("/"):
            if user_input == "/help":
                print(HELP)
            elif user_input == "/exit":
                print("Bye!")
                break
            else:
                print("Unknown command")
        elif not is_brackets(user_input):
            print(ERROR_EXPRESSION)
        elif user_input.isalpha() or is_number(user_input):
            print(variables[user_input] if user_input in variables.keys() else
                  int(user_input) if is_number(user_input) else ERROR_VARIABLE)
        elif "=" in user_input:
            variables_validation(user_input, variables)
        else:
            try:
                numbers = user_input.replace("(", "( ").replace(")", " )").split()
                numbers = [variables[num] if num.isalpha() else num for num in numbers]
            except KeyError:
                print(ERROR_IDENTIFIER)
            else:
                numbers = infix_to_postfix(numbers)
                print(smart_calculator(numbers))


main()

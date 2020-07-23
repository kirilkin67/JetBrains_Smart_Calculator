# write your code here
PLUS = "+"
MINUS = "-"
ERROR_EXPRESSION = "Invalid expression"
ERROR_IDENTIFIER = "Invalid identifier"
ERROR_VARIABLE = "Unknown variable"
HELP = """The program calculates:
-addition of numbers
-subtraction of numbers
-close program -> '/exit'"""


def add_numbers(num1, num2):
    try:
        return int(num1) + int(num2)
    except (ValueError, IndexError):
        return ERROR_EXPRESSION


def sub_numbers(num1, num2):
    try:
        return int(num1) - int(num2)
    except (ValueError, IndexError):
        return ERROR_EXPRESSION


def operator_definition(operator):
    if operator[0] == PLUS:
        return PLUS
    else:
        return PLUS if len(operator) % 2 == 0 else MINUS


def is_operator(operator):
    if operator.startswith((PLUS, MINUS)):
        if operator.count(PLUS) == len(operator) or \
                operator.count(MINUS) == len(operator):
            return True
    return False


def is_number(number):
    if (number[0] == MINUS or number[0] == PLUS) and number[1:].isdigit():
        return True
    return number.isdigit()


def smart_calculator(numbers):
    try:
        result = int(numbers[0])
    except (ValueError, IndexError):
        return ERROR_EXPRESSION
    else:
        for n in range(1, len(numbers), 2):
            if is_operator(numbers[n]):
                if operator_definition(numbers[n]) == PLUS:
                    result = add_numbers(result, numbers[n + 1])
                if operator_definition(numbers[n]) == MINUS:
                    result = sub_numbers(result, numbers[n + 1])
            else:
                return ERROR_EXPRESSION
        return result


def main():
    while True:
        user_input = input()
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
        else:
            validation(user_input)
            numbers = user_input.split()
            print(smart_calculator(numbers))


main()

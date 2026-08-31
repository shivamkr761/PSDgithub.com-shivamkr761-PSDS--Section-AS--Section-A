# 1. Infix to Postfix Conversion

from django.db.models import Expression


class OperatorStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = OperatorStack()
    postfix = ""

    for char in expression:
        if char.isalnum():
            postfix += char

        elif char == '(':
            stack.push(char)

        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '('

        else:
            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(char)):
                postfix += stack.pop()

            stack.push(char)

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Infix Expression:", expression)
print("Postfix Expression:", result)


# 2.Postfix Expression

class IntegerStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def evaluate_postfix(expression):
    stack = IntegerStack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))

        elif char in '+-*/':
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.push(result)

    return stack.pop()

expression = input("Enter postfix expression: ")

result = evaluate_postfix(expression)

print("Postfix Expression:", expression)
print("Final Result:", result)
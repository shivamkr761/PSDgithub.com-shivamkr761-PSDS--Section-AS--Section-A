# 1. Infix to Postfix Conversion


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

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()


def evaluate(expression):
    s = Stack()

    for ch in expression:
        if ch.isdigit():
            s.push(int(ch))
        else:
            b = s.pop()
            a = s.pop()

            if ch == '+':
                s.push(a + b)
            elif ch == '-':
                s.push(a - b)
            elif ch == '*':
                s.push(a * b)
            elif ch == '/':
                s.push(a // b)

    return s.pop()


expression = input("Enter postfix expression: ")
print("Result:", evaluate(expression))

3. Implement a binary
# search tree with insertion, deletion, and traversal operations (inorder,
# preorder, postorder). 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def minimum(root):
    while root.left:
        root = root.left
    return root


def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp = minimum(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

values = [28, 30, 69, 26, 47, 61, 84]

for value in values:
    root = insert(root, value)

print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

root = delete(root, 30)

print("\n\nAfter deleting 30:")
print("Inorder:", end=" ")
inorder(root)
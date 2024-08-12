def prec(self, c):
    precedence = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1}
    return precedence.get(c, -1)


def InfixtoPostfix(self, s):
    # code here

    stack = []  # Use a list as a stack
    result = []

    for c in s:
        if c.isalnum():  # Check if c is an operand (a-z, A-Z, or 0-9)
            result.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:  # It's an operator
            while stack and self.prec(c) <= self.prec(stack[-1]):
                result.append(stack.pop())
            stack.append(c)

    # Pop all the remaining elements from the stack
    while stack:
        result.append(stack.pop())

    # Join the result list into a string
    return "".join(result)

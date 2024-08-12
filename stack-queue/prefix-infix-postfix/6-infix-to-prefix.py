# infix_to_prefix.py


def infix_to_prefix(expression):
    # Function to check if the character is an operator
    def prec(c):
        precedence = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1}
        return precedence.get(c, -1)

    # Function to convert infix to prefix
    def convert(expression):
        stack = []
        prefix = []
        expression = expression[::-1]  # Reverse the infix expression

        for char in expression:
            if char.isalnum():  # If the character is an operand
                prefix.append(char)
            elif char == ")":
                stack.append(char)
            elif char == "(":
                while stack and stack[-1] != ")":
                    prefix.append(stack.pop())
                stack.pop()  # Remove ')'
            else:  # Operator
                while stack and prec(stack[-1]) > prec(char):
                    prefix.append(stack.pop())
                stack.append(char)

        while stack:
            prefix.append(stack.pop())

        return "".join(prefix[::-1])  # Reverse to get the correct prefix

    return convert(expression)


# Example usage
if __name__ == "__main__":
    infix_expr = "(A-B/C)*(A/K-L)"
    print("Prefix expression:", infix_to_prefix(infix_expr))

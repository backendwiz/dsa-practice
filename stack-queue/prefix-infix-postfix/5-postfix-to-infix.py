# postfix_to_infix.py


def postfix_to_infix(expression):
    stack = []

    for char in expression:
        if char.isalnum():  # If the character is an operand
            stack.append(char)
        else:  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Form the infix expression with parentheses
            new_expr = "({}{}{})".format(
                operand1, char, operand2
            )  # Using format method
            # new_expr = char + operand1 + operand2
            stack.append(new_expr)

    return stack[-1]  # The final expression is at the top of the stack


# Example usage
if __name__ == "__main__":
    postfix_expr = "ABC/-AK/L-*"
    print("Infix expression:", postfix_to_infix(postfix_expr))

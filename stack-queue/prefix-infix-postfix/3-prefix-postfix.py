# prefix_to_postfix.py


def prefix_to_postfix(expression):
    stack = []

    # Reverse the prefix expression for easier processing
    expression = expression[::-1]

    for char in expression:
        if char.isalnum():  # If the character is an operand
            stack.append(char)
        else:  # Operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Form the postfix expression
            # new_expr = "{} {} {}".format(operand1, operand2, char)
            new_expr = operand1 + operand2 + char  # Using format method
            stack.append(new_expr)

    return stack[-1]  # The final expression is at the top of the stack


# Example usage
if __name__ == "__main__":
    prefix_expr = "*-A/Bc-/AkL"
    print("Postfix expression:", prefix_to_postfix(prefix_expr))

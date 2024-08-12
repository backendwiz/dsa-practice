# prefix_to_infix.py


def prefix_to_infix(expression):
    stack = []

    # Reverse the prefix expression for easier processing
    expression = expression[::-1]

    for char in expression:
        if char.isalnum():  # If the character is an operand
            stack.append(char)
        else:  # Operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Form the infix expression with parentheses
            # new_expr = "({} {} {})".format(
            #     operand1, char, operand2
            # )  # Using format method
            new_expr = operand1 + char + operand2
            stack.append(new_expr)

    return stack[-1]  # The final expression is at the top of the stack


# Example usage
if __name__ == "__main__":
    prefix_expr = "*-A/Bc-/AkL"
    print("Infix expression:", prefix_to_infix(prefix_expr))

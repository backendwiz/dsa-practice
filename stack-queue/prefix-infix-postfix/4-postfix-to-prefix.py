# postfix_to_prefix.py


def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():  # If the character is an operand
            stack.append(char)
        else:  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Form the prefix expression
            new_expr = char + operand1 + operand2  # Using format method
            stack.append(new_expr)

    return stack[-1]  # The final expression is at the top of the stack


# Example usage
if __name__ == "__main__":
    postfix_expr = "ABC/-AK/L-*"
    print("Prefix expression:", postfix_to_prefix(postfix_expr))

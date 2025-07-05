def calculator():
    print("Welcome to the Python Calculator!")
    print("You can use +, -, *, /, ** (power), parentheses.")
    print("Type 'exit' to quit.\n")
    while True:
        expr = input('Enter calculation: ')
        if expr.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            # Only allow numbers and operators for safety
            allowed_chars = "0123456789+-*/(). "
            if any(c not in allowed_chars for c in expr):
                raise ValueError("Invalid character detected.")
            result = eval(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()

import re

filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

    # Regular expression pattern for identifying expressions
    expression_pattern = r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))'

    # Extract all expressions: `do()`, `don't()`, and `mul(X,Y)`
    expressions = re.findall(expression_pattern, content)

    # Initialize in a "do" state
    do_state = True

    # List to store matched mul expressions when in "do" state
    captured_mul_expressions = []

    # Iterate through the expressions
    for expr in expressions:
        if expr == 'do()':
            do_state = True
        elif expr == "don't()":
            do_state = False
        elif do_state and expr.startswith('mul('):
            # Extract numbers from the mul expression
            x, y = re.findall(r'\d+', expr)
            x, y = int(x), int(y)
            product = x * y
            captured_mul_expressions.append((x, y, product))

    result = 0

    # Print the captured expressions and their products
    for x, y, product in captured_mul_expressions:
        result += product

    print(f"Result: {result}")
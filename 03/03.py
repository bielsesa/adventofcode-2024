import re

filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

    # Regular expression pattern to match `mul(X,Y)` where X and Y are numbers with no spaces
    pattern = r'mul\((\d+),(\d+)\)'
    # This regex also captures X and Y directly and returns them as tuples, creating a full list of all the
    # captured numbers as tuples.

    # Find all matches in the input text
    matches = re.findall(pattern, content)

    result = 0

    # Iterate over each match
    for x, y in matches:
        # Convert X and Y to integers
        x = int(x)
        y = int(y)

        # Calculate the product
        product = x * y

        # Sum the product to the result
        result += product

    print(f"Result: {result}")
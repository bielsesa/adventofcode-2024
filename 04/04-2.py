filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

def find_x_mas(grid):
    # Define diagonal directions: down-right, down-left, up-right, up-left
    down_right = (1, 1) # down and right
    down_left = (1, -1) # down and left
    up_right = (-1, 1) # up and right
    up_left = (-1, -1) # up and left
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 'A':
                continue

            new_down_right = (i + down_right[0], j + down_right[1])
            new_down_left = (i + down_left[0], j + down_left[1])
            new_up_right = (i + up_right[0], j + up_right[1])
            new_up_left = (i + up_left[0], j + up_left[1])

            # Check if any of the diagonal positions are out of grid bounds
            if (new_down_right[0] >= len(grid) or new_down_right[1] >= len(grid[0]) or
                new_down_left[0] >= len(grid) or new_down_left[1] < 0 or
                new_up_right[0] < 0 or new_up_right[1] >= len(grid[0]) or
                new_up_left[0] < 0 or new_up_left[1] < 0):
                continue

            match = 0

            if (grid[new_down_right[0]][new_down_right[1]] == 'S' and grid[new_up_left[0]][new_up_left[1]] == 'M') \
                or (grid[new_down_right[0]][new_down_right[1]] == 'M' and grid[new_up_left[0]][new_up_left[1]] == 'S'):
                match += 1

            if (grid[new_down_left[0]][new_down_left[1]] == 'S' and grid[new_up_right[0]][new_up_right[1]] == 'M') \
                or (grid[new_down_left[0]][new_down_left[1]] == 'M' and grid[new_up_right[0]][new_up_right[1]] == 'S'):
                match += 1

            if match == 2:
                count += 1

    return count

# Convert content into a 2D character grid
content_grid = [list(line) for line in content.split('\n') if line.strip()]

# Find occurrences of the word 'MAS'
occurrences = find_x_mas(content_grid)
print(f"Occurrences of 'X-MAS': {occurrences}")

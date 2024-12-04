filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

def find_word(grid, word):
    # Define directions: right, left, up, down, diagonal down-right, diagonal down-left, diagonal up-right, diagonal up-left
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (-1, 0),  # up
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]
    count = 0
    word_len = len(word)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for dir_x, dir_y in directions:
                match = True
                for k in range(word_len):
                    new_x, new_y = i + k * dir_x, j + k * dir_y
                    # Check if the new indices are within grid boundaries
                    if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] != word[k]:
                        match = False
                        break
                if match:
                    count += 1
    return count

# Convert content into a 2D character grid
content_grid = [list(line) for line in content.split('\n') if line.strip()]

# Find occurrences of the word 'XMAS'
occurrences = find_word(content_grid, 'XMAS')
print(f"Occurrences of 'XMAS': {occurrences}")

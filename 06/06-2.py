filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

map = [list(line) for line in content.strip().split('\n')]

directions = ['^', '>', 'v', '<']

# First, find the guard's starting position
for i, row in enumerate(map):
    for j, char in enumerate(row):
        if char in directions:
            start_position = (i, j)
            break

is_edge_of_map = False
current_position = start_position
position_history = [start_position]
direction = directions.index(map[start_position[0]][start_position[1]])

def check_obstacle(map, position):
    return map[position[0]][position[1]] == '#'

def check_edge_of_map(map, position):
    return (position[0] < 0 or position[0] >= len(map) or 
            position[1] < 0 or position[1] >= len(map[0]))

while not is_edge_of_map:
    # Move the guard forward in the direction she's facing
    if directions[direction] == '^':
        # Before moving, check if the guard is about to hit an obstacle or to get to the edge of the map
        new_position = (current_position[0] - 1, current_position[1])
        if check_edge_of_map(map, new_position):
            is_edge_of_map = True
            break
        elif check_obstacle(map, new_position):
            # If so, turn right
            direction = (direction + 1) % 4
        else:   
            # Move up
            current_position = new_position
    elif directions[direction] == '>':
        # Before moving, check if the guard is about to hit an obstacle or to get to the edge of the map
        new_position = (current_position[0], current_position[1] + 1)
        if check_edge_of_map(map, new_position):
            is_edge_of_map = True
            break
        elif check_obstacle(map, new_position):
            # If so, turn right
            direction = (direction + 1) % 4
        else:   
            # Move right
            current_position = new_position
    elif directions[direction] == 'v':
        # Before moving, check if the guard is about to hit an obstacle or to get to the edge of the map
        new_position = (current_position[0] + 1, current_position[1])
        if check_edge_of_map(map, new_position):
            is_edge_of_map = True
            break
        elif check_obstacle(map, new_position):
            # If so, turn right
            direction = (direction + 1) % 4
        else:   
            # Move down
            current_position = new_position
    elif directions[direction] == '<':
        # Before moving, check if the guard is about to hit an obstacle or to get to the edge of the map    
        new_position = (current_position[0], current_position[1] - 1)
        if check_edge_of_map(map, new_position):
            is_edge_of_map = True
            break
        elif check_obstacle(map, new_position):
            # If so, turn right
            direction = (direction + 1) % 4
        else:   
            # Move left
            current_position = new_position
    
    if current_position not in position_history:
        position_history.append(current_position)

result = len(position_history)

print(result)

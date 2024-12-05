filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

    # Split content into lines
    lines = content.strip().split('\n')

    # Dictionary to store key-value mappings
    printing_rules = {}

    # Array to store the updates to be printed
    updates = []

    def process_lines(lines):
        printing_rules = {}
        updates = []
        
        # Process each line
        for line in lines:
            if '|' in line:  # Only process lines with key-value pairs
                key, value = line.split('|')
                # Add value to list for this key, creating list if key doesn't exist
                key = int(key)
                value = int(value)
                if key not in printing_rules:
                    printing_rules[key] = []
                printing_rules[key].append(value)
            else:
                # Split the update string by comma and convert to integers
                if line:  # Check if line is not empty
                    updates.append([int(x) for x in line.split(',')])
        return printing_rules, updates
    
    printing_rules, updates = process_lines(lines)

    invalid_updates = []
    
    def check_update_validity(update_array, printing_rules):
        is_valid = True
        for update in update_array:
            for key, values in printing_rules.items():
                if update == key:
                    for value in values:
                        # Look in update_array up to current update
                        for i in range(update_array.index(update)):
                            if update_array[i] == value:
                                is_valid = False
        return is_valid

    for update_array in updates:
        if not check_update_validity(update_array, printing_rules):
            invalid_updates.append(update_array)

    def reorder_invalid_updates(invalid_updates, printing_rules):
        new_invalid_updates = []
        for update_array in invalid_updates:
            # Convert to list if it's not already
            current_array = list(update_array)
            
            # Process all required swaps
            changed = True
            while changed:
                changed = False
                for i, num in enumerate(current_array):
                    for key, values in printing_rules.items():
                        if num == key:
                            for value in values:
                                for j in range(i):
                                    if current_array[j] == value:
                                        # Perform the swap
                                        current_array[j], current_array[i] = current_array[i], current_array[j]
                                        changed = True
            
            new_invalid_updates.append(current_array)
        
        return new_invalid_updates
    
    reordered_updates = reorder_invalid_updates(invalid_updates, printing_rules)

    invalid_updates_numbers = []
    for update in reordered_updates:
        # Get the middle number
        invalid_updates_numbers.append(update[len(update) // 2])

    # Sum all the numbers
    print(sum(int(x) for x in invalid_updates_numbers))
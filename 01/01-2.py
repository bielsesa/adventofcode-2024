filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

    # Split content into lines and extract the two columns
    lines = content.strip().split('\n')
    first_list = []
    second_list = []
    
    for line in lines:
        # Split each line by space and append to respective lists
        first, second = line.split()
        first_list.append(first)
        second_list.append(second)

        # Convert strings to integers and sort both lists
        first_list = sorted([int(x) for x in first_list])
        second_list = sorted([int(x) for x in second_list])

    distances_list = []

    for number in first_list:
        count = second_list.count(number)
        distances_list.append(number * count)

    print(distances_list)

    print(sum(distances_list))


        



    


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

    for i in range(len(first_list)):
        distance = abs(first_list[i] - second_list[i])
        distances_list.append(distance)

    print(distances_list)

    print(sum(distances_list))


        



    


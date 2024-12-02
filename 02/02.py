filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

    reports = content.strip().split('\n')
    safe_reports = 0

    for report in reports:
        levels = report.split()
        # Convert levels to integers
        levels = [int(x) for x in levels]
        
        # Check if strictly increasing or decreasing
        is_increasing = all(levels[i] < levels[i+1] for i in range(len(levels)-1))
        is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels)-1))
        
        if is_increasing or is_decreasing:
            # Check if adjacent differences are between 1 and 3
            adjacent_diffs = [abs(levels[i] - levels[i+1]) for i in range(len(levels)-1)]
            if all(1 <= diff <= 3 for diff in adjacent_diffs):
                safe_reports += 1

    print(safe_reports)


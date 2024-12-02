filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()

    reports = content.strip().split('\n')
    safe_reports = 0

    def is_safe_report(levels):
        if len(levels) < 2:
            return False
            
        # Check if strictly increasing or decreasing
        is_increasing = all(levels[i] < levels[i+1] for i in range(len(levels)-1))
        is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels)-1))
        
        if not (is_increasing or is_decreasing):
            return False
            
        # Check if adjacent differences are between 1 and 3
        adjacent_diffs = [abs(levels[i] - levels[i+1]) for i in range(len(levels)-1)]
        return all(1 <= diff <= 3 for diff in adjacent_diffs)

    for report in reports:
        levels = report.split()
        # Convert levels to integers
        levels = [int(x) for x in levels]
        
        # Check original report
        if is_safe_report(levels):
            safe_reports += 1
            continue
            
        # Try removing one level at a time
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i+1:]
            if is_safe_report(modified_levels):
                safe_reports += 1
                break

    print(safe_reports)

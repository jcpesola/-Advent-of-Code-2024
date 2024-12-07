with open('day_2/input.txt', 'r') as file:
    input_data = file.read()

reports = input_data.strip().split('\n')
levels = [tuple(map(int, report.split())) for report in reports]
# print(levels)

#How many reports are safe?
#Safe report = numbers all increase/decrease by at least 1 and at most 3
#7, 6, 4, 2, 1

def is_safe_1(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return all_decreasing or all_increasing

def is_safe_2(report):
    if is_safe_1(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_1(modified_report):
            return True
    
    return False

safe_reports_1 = 0
safe_reports_2 = 0
for level in levels:
    if is_safe_1(level) == True:
       safe_reports_1 += 1
    if is_safe_2(level) == True:
        safe_reports_2 += 1

print("Part 1: ", safe_reports_1)
print("Part 2: ", safe_reports_2)

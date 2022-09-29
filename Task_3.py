inputLines = []
with open('/Users/volodia/Desktop/Python/DZ/DZ 4/Input_Task_3.txt', 'r') as file:
    inputLines = file.readlines()

outputLines = []
for line in inputLines:
    if (line.__contains__("5")):
        outputLines.append(line.upper())
    else:
        outputLines.append(line)

with open('/Users/volodia/Desktop/Python/DZ/DZ 4/Input_Task_3.txt', 'w') as file:
    for line in outputLines:
        file.write(line)
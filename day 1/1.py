import re

with open("input.txt") as f:
    lines = f.readlines()

count = 0
for line in lines:
    digits = re.findall("\d", line)
    count += int(str(digits[0]) + str(digits[-1]))

print(count)

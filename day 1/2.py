import re

with open("input.txt") as f:
    lines = f.readlines()

word_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


count = 0
pattern = r"(\d|" + "|".join(word_to_number.keys()) + r")"

for line in lines:
    line = (
        line.replace("one", "oonee")
        .replace("two", "ttwoo")
        .replace("three", "tthreee")
        .replace("four", "ffourr")
        .replace("five", "ffivee")
        .replace("six", "ssixx")
        .replace("seven", "ssevenn")
        .replace("eight", "eeightt")
        .replace("nine", "nninee")
    )
    digits = re.findall(pattern, line)
    first_digit = word_to_number.get(digits[0], str(digits[0]))
    last_digit = word_to_number.get(digits[-1], str(digits[-1]))
    count += int(first_digit + last_digit)

print(count)

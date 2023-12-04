import re

with open("input.txt") as f:
    lines = f.readlines()


def check(color, game):
    numbers = [int(r.strip(f" {color}")) for r in re.findall("\d+ " + color, game)]
    return numbers


def max_color(color, games):
    numbers = []
    for game in games:
        numbers += check(color, game)
    return max(numbers) if len(numbers) > 0 else 0


count = 0
for line in lines:
    games = re.sub("Game \d+:", "", line).split(";")
    game_number = re.findall("Game (\d+):", line)[0]
    max_red = max_color("red", games)
    max_green = max_color("green", games)
    max_blue = max_color("blue", games)

    count += max_red * max_blue * max_green


print(count)

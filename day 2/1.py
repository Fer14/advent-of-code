import re

with open("input.txt") as f:
    lines = f.readlines()


def check(color, n, game):
    numbers = [int(r.strip(f" {color}")) for r in re.findall("\d+ " + color, game)]
    return numbers[0] <= n if len(numbers) > 0 else True


count = 0
for line in lines:
    games = re.sub("Game \d+:", "", line).split(";")
    game_number = re.findall("Game (\d+):", line)[0]
    imposible = True
    for game in games:
        if (
            check("red", 12, game)
            and check("green", 13, game)
            and check("blue", 14, game)
        ):
            imposible = False
    if imposible:
        count += int(game_number)

print(count)

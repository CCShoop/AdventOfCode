file = open('input.txt', 'r')

class Pull:
    def __init__(self, red:int = 0, green:int = 0, blue:int = 0):
        self.red = red
        self.green = green
        self.blue = blue

class Game:
    def __init__(self, id:int):
        self.id = id
        self.pulls = []

    def add_pull(self, red:int, green:int, blue:int):
        self.pulls.append(Pull(red=red, green=green, blue=blue))


games = []

for line in file:
    parseId, parseGames = line.split(':')
    id = int(parseId[5:])
    game = Game(id)
    for pull in parseGames.strip().split(';'):
        colors = pull.split(',')
        redCount = 0
        greenCount = 0
        blueCount = 0
        for color in colors:
            color = color.strip().split(' ')
            if 'red' in color[1]:
                redCount = int(color[0])
            elif 'green' in color[1]:
                greenCount = int(color[0])
            elif 'blue' in color[1]:
                blueCount = int(color[0])
        game.add_pull(red=redCount, green=greenCount, blue=blueCount)
    games.append(game)

# for game in games:
#     print(f'Game {game.id}')
#     for pull in game.pulls:
#         print(f'\tRed: {pull.red}, Green: {pull.green}, Blue: {pull.blue}')


# Part 1
RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14
id_sum = 0

for game in games:
    valid = True
    for pull in game.pulls:
        if pull.red > RED_LIMIT or pull.green > GREEN_LIMIT or pull.blue > BLUE_LIMIT:
            valid = False
    if valid:
        id_sum += game.id

print(f'Part 1: {id_sum}')
# 5050 is TOO HIGH
# 2505 is the answer


# Part 2
power_sum = 0

for game in games:
    min_red = 0
    min_green = 0
    min_blue = 0
    for pull in game.pulls:
        if pull.red > min_red: min_red = pull.red
        if pull.green > min_green: min_green = pull.green
        if pull.blue > min_blue: min_blue = pull.blue
    game_power = min_red * min_green * min_blue
    power_sum += game_power

print(f'Part 2: {power_sum}')
# 70265 is the answer


file.close()

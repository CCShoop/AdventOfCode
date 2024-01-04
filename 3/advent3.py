file = open('input.txt', 'r')

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LAST_ROW = 140
LAST_COLUMN = 139

schematic = []
for line in file:
    segment = []
    line = line.strip()
    for char in line:
        segment.append(char)
    schematic.append(segment)

# for segment in schematic:
#     line = ''
#     for char in segment:
#         line += char
#     print(line)


class PartIdentifier:
    def __init__(self, char, x:int, y:int):
        self.char = char
        self.x = x
        self.y = y

class PossiblePart:
    def __init__(self, value:int, x_range:list, y:int):
        self.value = value
        self.x_range = x_range.copy()
        self.y = y
        self.isPart = False

class SchematicData:
    def __init__(self):
        self.partIdentifiers = []
        self.possibleParts = []
        self.engineParts = []


schematicData = SchematicData()
inNumber = False
y = 0
for segment in schematic:
    possiblePartPart = ''
    x_range = []
    x = 0
    for char in segment:
        if char in NUMBERS:
            inNumber = True
            possiblePartPart += char
            x_range.append(x)
        elif char != '.':
            if inNumber:
                inNumber = False
                # print(f'Possible Part {int(possiblePartPart)}:\n\t\tx_range: {x_range}\n\t\ty: {y}\n')
                possiblePart = PossiblePart(int(possiblePartPart), x_range, y)
                schematicData.possibleParts.append(possiblePart)
                possiblePartPart = ''
                x_range.clear()
            print(f'Part Identifier {char}: x = {x}, y = {y}\n')
            schematicData.partIdentifiers.append(PartIdentifier(char, x, y))
        else:
            if inNumber:
                inNumber = False
                # print(f'Possible Part {int(possiblePartPart)}:\n\t\tx_range: {x_range}\n\t\ty: {y}\n')
                possiblePart = PossiblePart(int(possiblePartPart), x_range, y)
                schematicData.possibleParts.append(possiblePart)
                possiblePartPart = ''
                x_range.clear()
        x += 1
    if inNumber:
        inNumber = False
        # print(f'Possible Part {int(possiblePartPart)}:\n\t\tx_range: {x_range}\n\t\ty: {y}\n')
        possiblePart = PossiblePart(int(possiblePartPart), x_range, y)
        schematicData.possibleParts.append(possiblePart)
        possiblePartPart = ''
        x_range.clear()
    y += 1


def isPartIdentifier(x, y):
    for partIdentifier in schematicData.partIdentifiers:
        if partIdentifier.x == x and partIdentifier.y == y:
            print(f'part identifier {partIdentifier.char} at x = {partIdentifier.x}, y = {partIdentifier.y}')
            return True
    return False


def isPartNumber(possiblePart: PossiblePart):
    print()
    # check char before/after on same line
    if possiblePart.x_range[0] > 0:
        if isPartIdentifier(possiblePart.x_range[0]-1, possiblePart.y):
            print(f'Is left ({possiblePart.x_range[0]-1}, {possiblePart.y}) {schematic[possiblePart.x_range[0]-1][possiblePart.y]}')
            return True
        print(f'Not left ({possiblePart.x_range[0]-1}, {possiblePart.y}) {schematic[possiblePart.x_range[0]-1][possiblePart.y]}')
    if possiblePart.x_range[len(possiblePart.x_range)-1] < LAST_COLUMN:
        if isPartIdentifier(possiblePart.x_range[len(possiblePart.x_range)-1]+1, possiblePart.y):
            print(f'Is right ({possiblePart.x_range[len(possiblePart.x_range)-1]+1}, {possiblePart.y}) {schematic[possiblePart.x_range[len(possiblePart.x_range)-1]+1][possiblePart.y]}')
            return True
        print(f'Not right ({possiblePart.x_range[len(possiblePart.x_range)-1]+1}, {possiblePart.y}) {schematic[possiblePart.x_range[len(possiblePart.x_range)-1]+1][possiblePart.y]}')

    # check chars in line above
    if possiblePart.y > 0:
        if possiblePart.x_range[0] > 0:
            if isPartIdentifier(possiblePart.x_range[0]-1, possiblePart.y-1):
                print(f'Is upper left ({possiblePart.x_range[0]-1}, {possiblePart.y-1}) {schematic[possiblePart.x_range[0]-1][possiblePart.y-1]}')
                return True
            print(f'Not upper left ({possiblePart.x_range[0]-1}, {possiblePart.y-1}) {schematic[possiblePart.x_range[0]-1][possiblePart.y-1]}')
        for x in possiblePart.x_range:
            if isPartIdentifier(x, possiblePart.y-1):
                print(f'Is above ({x}, {possiblePart.y-1}) {schematic[x][possiblePart.y-1]}')
                return True
            print(f'Not above ({x}, {possiblePart.y-1}) {schematic[x][possiblePart.y-1]}')
        if possiblePart.x_range[len(possiblePart.x_range)-1] < LAST_COLUMN:
            if isPartIdentifier(possiblePart.x_range[len(possiblePart.x_range)-1]+1, possiblePart.y-1):
                print(f'Is lower right ({possiblePart.x_range[len(possiblePart.x_range)-1]+1}, {possiblePart.y-1}) {schematic[possiblePart.x_range[len(possiblePart.x_range)-1]+1][possiblePart.y-1]}')
                return True
            print(f'Not lower right ({possiblePart.x_range[len(possiblePart.x_range)-1]+1}, {possiblePart.y-1}) {schematic[possiblePart.x_range[len(possiblePart.x_range)-1]+1][possiblePart.y-1]}')

    # check chars in line below
    if possiblePart.y < LAST_ROW:
        if possiblePart.x_range[0] > 0:
            if isPartIdentifier(possiblePart.x_range[0]-1, possiblePart.y+1):
                print(f'Is lower left () {schematic[possiblePart.x_range[0]-1][possiblePart.y+1]}')
                return True
            print(f'Not lower left () {schematic[possiblePart.x_range[0]-1][possiblePart.y+1]}')
        for x in possiblePart.x_range:
            if isPartIdentifier(x, possiblePart.y+1):
                print(f'Is below () {schematic[x][possiblePart.y+1]}')
                return True
            print(f'Not below () {schematic[x][possiblePart.y+1]}')
        if possiblePart.x_range[len(possiblePart.x_range)-1] < LAST_COLUMN:
            if isPartIdentifier(possiblePart.x_range[len(possiblePart.x_range)-1]+1, possiblePart.y+1):
                print(f'Is lower right () {schematic[possiblePart.x_range[len(possiblePart.x_range)-1]+1][possiblePart.y+1]}')
                return True
            print(f'Not lower right () {schematic[possiblePart.x_range[len(possiblePart.x_range)-1]+1][possiblePart.y+1]}')

    return False


for possiblePart in schematicData.possibleParts:
    possiblePart.isPart = isPartNumber(possiblePart)
    print(f'value: {possiblePart.value}, x_range: {possiblePart.x_range}, y: {possiblePart.y}\n')
    if possiblePart.isPart:
        schematicData.engineParts.append(possiblePart)


# Part 1
partSum = 0
for enginePart in schematicData.engineParts:
    partSum += enginePart.value
print(f'Part 1: {partSum}')
# 304869 is too low

# Part 2




file.close()
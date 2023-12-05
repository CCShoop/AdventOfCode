file = open('input.txt', 'r')

schematic = []
for line in file:
    segment = []
    for char in line:
        segment.append(char)
    schematic.append(segment)

# for segment in schematic:
#     line = ''
#     for char in segment:
#         line += char
#     print(line)

class SchematicData:
    def __init__(self, schematic):
        self.schematic = schematic
        self.engineParts = []
    
    def add_part(self, number):
        self.engineParts.append(number)

schematicData = SchematicData(schematic)

# parse document, tracking location
# previous previous line, previous line, current line
# (previous line), (current line), (next line)



# Part 1
partSum = 0
partSum += sum(schematicData.engineParts)
print(f'Part 1: {partSum}')


# Part 2




file.close()
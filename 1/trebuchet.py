import re

# Part 1
values = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        numbers = ''
        for char in line:
            if not char.isalpha():
                numbers += char
        number = numbers[0] + numbers[len(numbers)-1]
        values.append(int(number))
answer = 0
for value in values:
    answer += value
print(f'Part 1: {answer}')
# 55447 is the answer

# Part 2
values = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        while 'one' in line:
            line = line.replace('one', 'o1ne')
        while 'two' in line:
            line = line.replace('two', 'tw2o')
        while 'three' in line:
            line = line.replace('three', 'thr3ee')
        while 'four' in line:
            line = line.replace('four', 'fo4ur')
        while 'five' in line:
            line = line.replace('five', 'fi5ve')
        while 'six' in line:
            line = line.replace('six', 'si6x')
        while 'seven' in line:
            line = line.replace('seven', 'sev7en')
        while 'eight' in line:
            line = line.replace('eight', 'ei8ght')
        while 'nine' in line:
            line = line.replace('nine', 'ni9ne')
        numbers = ''
        for char in line:
            if not char.isalpha():
                numbers += char
        number = numbers[0] + numbers[len(numbers)-1]
        values.append(int(number))
answer = 0
for value in values:
    answer += value
print(f'Part 2: {answer}')
# 54706 is the answer

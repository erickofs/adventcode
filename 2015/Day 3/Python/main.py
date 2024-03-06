"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, 
and then an elf at the North Pole calls him via radio and tells him where to move next. 
Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, 
and so his directions are a little off, and Santa ends up visiting some houses more than once. 

How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""
# Define a list called houses
# Open the file in read mode as input
    # Define the starting position as (0,0)
    # Define the position as a tuple (x,y)
    # cline = input.readline().strip()
    # While cline:
        # Append the starting position to the list houses
        # For each character in cline:
            # If the character is '^':
                # y += 1
                # Append position to the list houses
            # If the character is 'v':
                # y -= 1
                # Append position to the list houses
            # If the character is '>':
                # x += 1
                # Append position to the list houses
            # If the character is '<':
                # x -= 1
                # Append position to the list houses
            # cline = input.readline().strip()
# Remove duplicates from the list houses
# Print the length of the list houses

with open('input.txt', 'r') as input:
    houses = []
    x = 0
    y = 0
    start = [x,y]
    houses.append(start)
    position = [x,y]
    cline = input.readline().strip()
    while cline:
        for char in cline:
            if char == '^':
                position[1] += 1
                houses.append(position.copy())
            if char == 'v':
                position[1] -= 1
                houses.append(position.copy())
            if char == '>':
                position[0] += 1
                houses.append(position.copy())
            if char == '<':
                position[0] -= 1
                houses.append(position.copy())
        cline = input.readline().strip()
    houses = list(set(map(tuple, houses)))
    print(f'The number of houses that receive at least one present is {len(houses)}')

"""
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""

with open('input.txt', 'r') as input:
    houses = []
    x = 0
    y = 0
    start = [x,y]
    houses.append(start)
    s_position = [x,y]
    r_position = [x,y]
    cline = input.readline().strip()
    while cline:
        for i, char in enumerate(cline):
            if i % 2 == 0:
                if char == '^':
                    s_position[1] += 1
                    houses.append(s_position.copy())
                if char == 'v':
                    s_position[1] -= 1
                    houses.append(s_position.copy())
                if char == '>':
                    s_position[0] += 1
                    houses.append(s_position.copy())
                if char == '<':
                    s_position[0] -= 1
                    houses.append(s_position.copy())
            else:
                if char == '^':
                    r_position[1] += 1
                    houses.append(r_position.copy())
                if char == 'v':
                    r_position[1] -= 1
                    houses.append(r_position.copy())
                if char == '>':
                    r_position[0] += 1
                    houses.append(r_position.copy())
                if char == '<':
                    r_position[0] -= 1
                    houses.append(r_position.copy())
        cline = input.readline().strip()
    houses = list(set(map(tuple, houses)))
    print(f'The number of houses that receive at least one present is {len(houses)}')
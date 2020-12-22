'''
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''

tree_map = []

with open('data/day3.txt', 'r') as file:
    while True:
        line = file.readline().strip('\n')
        if not line:
            break
        tree_map.append(line)

map_length = len(tree_map[0])

def num_trees_encountered(right, down):
    num_trees = 0
    start_pos = 0
    for row_num in range(0, len(tree_map), down):
        if tree_map[row_num][start_pos % map_length] == '#':
            num_trees += 1
        
        start_pos += right

    return num_trees

print(num_trees_encountered(1, 1) * 
      num_trees_encountered(3, 1) * 
      num_trees_encountered(5, 1) *
      num_trees_encountered(7, 1) *
      num_trees_encountered(1, 2))
'''
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
'''

seats = []
row = []

with open('data/day11.txt', 'r') as file:
    while True:
        c = file.read(1)

        if not c:
            break
        
        if c == '\n':
            seats.append(row)
            row = []
        else:
            row.append(c)


def swap(char):
    return '#' if char == 'L' else 'L'


def count_adj_seats(row, col):
    orig_row = row
    orig_col = col

    num_adjacent_seats = 0

    # Left
    try:
        row = orig_row
        col = orig_col

        if col == 0:
            raise IndexError

        while seats[row][col - 1] == '.':
            col -= 1 
            if col == 0:
                raise IndexError

        if seats[row][col - 1] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Right
    try:
        row = orig_row
        col = orig_col

        while seats[row][col + 1] == '.':
            col += 1

        if seats[row][col + 1] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Up
    try:
        row = orig_row
        col = orig_col

        if row == 0:
            raise IndexError

        while seats[row - 1][col] == '.':
            row -= 1
            if row == 0:
                raise IndexError

        if seats[row - 1][col] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Down
    try:
        row = orig_row
        col = orig_col

        while seats[row + 1][col] == '.':
            row += 1

        if seats[row + 1][col] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Up Left
    try:
        row = orig_row
        col = orig_col

        if row == 0 or col == 0:
            raise IndexError

        while seats[row - 1][col - 1] == '.':
            row -= 1
            col -= 1
            if row == 0 or col == 0:
                raise IndexError

        if seats[row - 1][col - 1] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Up Right
    try:
        row = orig_row
        col = orig_col

        if row == 0:
            raise IndexError

        while seats [row - 1][col + 1] == '.':
            row -= 1
            col += 1
            if row == 0:
                raise IndexError

        if seats[row - 1][col + 1] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Down Left
    try:
        row = orig_row
        col = orig_col

        if col == 0:
            raise IndexError

        while seats[row + 1][col - 1] == '.':
            row += 1
            col -= 1
            if col == 0:
                raise IndexError

        if seats[row + 1][col - 1] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    # Down Right
    try:
        row = orig_row
        col = orig_col

        while seats[row + 1][col + 1] == '.':
            row += 1
            col += 1

        if seats[row + 1][col + 1] == '#':
            num_adjacent_seats += 1

    except IndexError:
        pass

    return num_adjacent_seats


def scan_seats():
    seats_count = []
    rows_count = []

    for row in range(len(seats)):
        for col in range(len(seats[0])):
            rows_count.append(count_adj_seats(row, col))
        seats_count.append(rows_count)
        rows_count = []

    return seats_count


def update_seats():
    global seats

    seats_count = scan_seats()

    done = True

    for i in range(len(seats_count)):
        for j in range(len(seats_count[0])):
            if seats[i][j] != '.':
                if seats_count[i][j] == 0 and seats[i][j] == 'L':
                    seats[i][j] = swap(seats[i][j])
                    done = False
                    
                if seats_count[i][j] >= 5 and seats[i][j] == '#':
                    seats[i][j] = swap(seats[i][j])
                    done = False

    if done:
        occupied_seats = 0
        for row in seats:
            for seat in row:
                if seat == '#':
                    occupied_seats += 1
        
        return occupied_seats

    return update_seats()


print(update_seats())
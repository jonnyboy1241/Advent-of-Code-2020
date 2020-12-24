'''
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

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

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

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

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
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
    num_adjacent_seats = 0

    # Left
    try:
        if col == 0:
            raise IndexError
        if seats[row][col - 1] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Right
    try: 
        if seats[row][col + 1] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Up
    try:
        if row == 0:
            raise IndexError
        if seats[row - 1][col] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Down
    try:
        if seats[row + 1][col] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Up Left
    try:
        if row == 0 or col == 0:
            raise IndexError
        if seats[row - 1][col - 1] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Up Right
    try:
        if row == 0:
            raise IndexError
        if seats[row - 1][col + 1] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Down Left
    try:
        if col == 0:
            raise IndexError
        if seats[row + 1][col - 1] == '#':
            num_adjacent_seats += 1
    except IndexError:
        pass

    # Down Right
    try:
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
                    
                if seats_count[i][j] >= 4 and seats[i][j] == '#':
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
'''
--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?
'''

directions = []

with open('data/day12.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip('\n')
        directions.append([line[0], int(line[1:])])

ship_location = [0, 0]
waypoint_location = [10, 1]


def north(val):
    waypoint_location[1] += val


def south(val):
    waypoint_location[1] -= val


def east(val):
    waypoint_location[0] += val


def west(val):
    waypoint_location[0] -= val


def clockwise_90():
    global waypoint_location

    x = waypoint_location[0]
    y = waypoint_location[1]
    waypoint_location = [y, -x]


def clockwise_180():
    global waypoint_location

    x = waypoint_location[0]
    y = waypoint_location[1]
    waypoint_location = [-x, -y]


def clockwise_270():
    global waypoint_location

    x = waypoint_location[0]
    y = waypoint_location[1]
    waypoint_location = [-y, x]

def turn_right(val):
    if val == 90:
        clockwise_90()
    elif val == 180:
        clockwise_180()
    elif val == 270:
        clockwise_270()
    else:
        print('ERROR')


def turn_left(val):
    if val == 90:
        clockwise_270()
    elif val == 180:
        clockwise_180()
    elif val == 270:
        clockwise_90()
    else:
        print('ERROR')


def move_forward(val):
    global ship_location

    ship_location[0] += (val * waypoint_location[0])
    ship_location[1] += (val * waypoint_location[1])

    
def direction_handler(direction, val):
    if direction == 'N':
        north(val)

    elif direction == 'S':
        south(val)

    elif direction == 'E':
        east(val)

    elif direction == 'W':
        west(val)

    elif direction == 'R':
        turn_right(val)

    elif direction == 'L':
        turn_left(val)

    elif direction == 'F':
        move_forward(val)


for direction in directions:
    direction_handler(direction[0], direction[1])


print(abs(ship_location[0]) + abs(ship_location[1]))
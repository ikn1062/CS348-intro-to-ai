import common


def drone_flight_planner(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # access the policies using "policies[y][x]"
    # access the values using "values[y][x]"
    # y between 0 and 5
    # x between 0 and 5
    # function must return the value of the cell corresponding to the starting position of the drone
    y_start, x_start = 0, 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 2:
                values[y][x] = delivery_fee
            if map[y][x] == 3:
                values[y][x] = -1 * dronerepair_cost
            if map[y][x] == 1:
                y_start, x_start = y, x

    while 1:
        brk = True
        for y in range(len(map)):
            for x in range(len(map[0])):
                max_Q = -10000000
                if map[y][x] != 2 and map[y][x] != 3:
                    prop = 1
                    for a in range(1, 9):
                        value = 0
                        if a > 4:
                            prop = 2
                        r = -1 * prop * battery_drop_cost
                        for s in calculate_next_states(y, x, a % 4, prop):
                            value += s[2] * (r + (discount * values[s[0]][s[1]]))
                        if value > max_Q:
                            max_Q = value
                            policies[y][x] = a
                    diff = max_Q - values[y][x]
                    values[y][x] = max_Q
                    if abs(diff) > 0.00001:
                        brk = False
        if brk:
            break
    return values[y_start][x_start]


def calculate_next_states(y, x, a, prop):
    action = {1: [1, 0], 2: [0, -1], 3: [-1, 0], 0: [0, 1]}
    d = action[a]
    d1 = d[::-1]
    d2 = [0, 0]
    for i in range(len(d1)):
        d2[i] = -d1[i]
    all_states = [d1, d2]
    
    result = []

    p = 0.7
    p1 = 0.15
    if prop == 2:
        p = 0.8
        p1 = 0.1

    y1, x1 = y + d[0], x + d[1]
    if y1 < 0 or x1 < 0 or y1 > 5 or x1 > 5:
        y1, x1 = y, x
    result.append([y1, x1, p])

    all_dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    for direction in all_dir:
        if direction in all_states:
            y1, x1 = y + direction[0], x + direction[1]
            if y1 < 0 or x1 < 0 or y1 > 5 or x1 > 5:
                y1, x1 = y, x
            result.append([y1, x1, p1])

    return result

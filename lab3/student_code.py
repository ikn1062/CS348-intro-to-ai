import common


def astar_search(map):
    found = False
    # Initialize visited, parent, and frontier
    y_max = len(map) - 1
    x_max = len(map[0]) - 1
    parent = [[0 for i in range(x_max + 1)] for j in range(y_max + 1)]
    past_cost = [[99 for i in range(x_max + 1)] for j in range(y_max + 1)]
    man_dist = [[99 for i in range(x_max + 1)] for j in range(y_max + 1)]
    est_cost = [[99 for i in range(x_max + 1)] for j in range(y_max + 1)]
    frontier = []

    # Find starting point of the map
    y_start, x_start = 0, 0
    for j in range(y_max + 1):
        for i in range(x_max + 1):
            if map[j][i] == 2:
                y_start, x_start = j, i
            if map[j][i] == 3:
                y_goal, x_goal = j, i
    frontier.append([y_start, x_start])

    past_cost[y_start][x_start] = 0
    for j in range(y_max + 1):
        for i in range(x_max):
            man_dist[j][i] = abs(x_goal - i) + abs(y_goal - j)
    est_cost[y_start][x_start] = man_dist[y_start][x_start]
    man_dist[y_goal][x_goal] = 0

    while len(frontier) > 0:
        pos = frontier.pop(0)
        y, x = pos[0], pos[1]
        if map[y][x] == 3:
            found = True
            map[y][x] = 5
            break
        map[y][x] = 4
        children = [[y, x - 1], [y - 1, x], [y + 1, x], [y, x + 1]]
        for c in children:
            if not (c[0] < 0 or c[0] > y_max or c[1] < 0 or c[1] > x_max or map[c[0]][c[1]] == 4 or map[c[0]][c[1]] == 1):
                frontier.append(c)
                if (past_cost[y][x] + 1) < past_cost[c[0]][c[1]]:
                    past_cost[c[0]][c[1]] = past_cost[y][x] + 1
                    est_cost[c[0]][c[1]] = past_cost[c[0]][c[1]] + man_dist[c[0]][c[1]]
                    parent[c[0]][c[1]] = pos
                for i in range(len(frontier)):
                    for j in range(len(frontier)-i-1):
                        y1, x1 = frontier[j][0], frontier[j][1]
                        y2, x2 = frontier[j+1][0], frontier[j+1][1]
                        if est_cost[y2][x2] < est_cost[y1][x1]:
                            frontier[j] = [y2, x2]
                            frontier[j+1] = [y1, x1]
    if found:
        while parent[y][x] != 0:
            curr_pos = parent[y][x]
            y, x = curr_pos[0], curr_pos[1]
            map[y][x] = 5
    return found

import common


def df_search(map):
	found = False
	# Initialize visited, parent, and frontier
	y_max = len(map)-1
	x_max = len(map[0])-1
	parent = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
	frontier = []

	# Find starting point of the map
	for i in range(y_max+1):
		for j in range(x_max):
			if map[i][j] == 2:
				y_start, x_start = i, j
	frontier.append([y_start, x_start])

	while len(frontier) > 0:
		pos = frontier.pop(-1)
		y, x = pos[0], pos[1]
		if map[y][x] == 3:
			found = True
			map[y][x] = 5
			break
		map[y][x] = 4
		children = [[y-1, x], [y, x-1], [y+1, x], [y, x+1]]
		for c in children:
			if not (c[0] < 0 or c[0] > y_max or c[1] < 0 or c[1] > x_max):
				if not(map[c[0]][c[1]] == 4 or map[c[0]][c[1]] == 1):
					frontier.append(c)
					parent[c[0]][c[1]] = pos

	if found:
		while parent[y][x] != 0:
			curr_pos = parent[y][x]
			y, x = curr_pos[0], curr_pos[1]
			map[y][x] = 5
	print(map)
	return found


def bf_search(map):
	found = False
	# Initialize visited, parent, and frontier
	y_max = len(map) - 1
	x_max = len(map[0]) - 1
	parent = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
	frontier = []

	# Find starting point of the map
	for i in range(y_max+1):
		for j in range(x_max):
			if map[i][j] == 2:
				y_start, x_start = i, j
	frontier.append([y_start, x_start])

	while len(frontier) > 0:
		pos = frontier.pop(0)
		y, x = pos[0], pos[1]
		if map[y][x] == 3:
			found = True
			map[y][x] = 5
			break
		map[y][x] = 4
		children = [[y, x+1], [y+1, x], [y, x-1], [y-1, x]]
		for c in children:
			if not (c[0] < 0 or c[0] > y_max or c[1] < 0 or c[1] > x_max):
				if not(map[c[0]][c[1]] == 4 or map[c[0]][c[1]] == 1):
					frontier.append(c)
					parent[c[0]][c[1]] = pos

	if found:
		while parent[y][x] != 0:
			curr_pos = parent[y][x]
			y, x = curr_pos[0], curr_pos[1]
			map[y][x] = 5
	print(map)
	return found


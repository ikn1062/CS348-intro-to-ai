import common


class Variables:
	counter = 0


def sudoku_backtracking(sudoku):
	Variables.counter = 0
	bt(sudoku)
	return Variables.counter


def sudoku_forwardchecking(sudoku):
	Variables.counter = 0
	ft(sudoku)
	return Variables.counter


def bt(sudoku):
	Variables.counter += 1
	if solved(sudoku):
		return True
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0:
				for num in range(1, 10):
					if common.can_yx_be_z(sudoku, y, x, num):
						sudoku[y][x] = num
						if bt(sudoku):
							return True
						sudoku[y][x] = 0
				return False


def ft(sudoku):
	Variables.counter += 1
	if solved(sudoku):
		return True
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0:
				for num in range(1, 10):
					if common.can_yx_be_z(sudoku, y, x, num):
						sudoku[y][x] = num
						if not gen_domain(sudoku):
							if ft(sudoku):
								return True
						sudoku[y][x] = 0
				return False


def solved(sudoku):
	result = True
	for y in range(9):
		for x in range(9):
			value = sudoku[y][x]
			sudoku[y][x] = 0
			if not (value != 0 and common.can_yx_be_z(sudoku, y, x, value)):
				result = False
			sudoku[y][x] = value
	return result


def gen_domain(sudoku):
	empty_domain = False
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0:
				empty_domain_val = True
				for num in range(1, 10):
					if common.can_yx_be_z(sudoku, y, x, num):
						empty_domain_val = False
				if empty_domain_val:
					empty_domain = True
	return empty_domain

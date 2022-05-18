import common


def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in index 0 and Y in index 1, and a blank space in index 2
	# to be filled with class
	# The class value could be a 0 or a 1
	w = [0, 0, 0]

	all_correct_class = False
	while not all_correct_class:
		all_correct_class = True
		for t in data_train:
			C = pone_classify(t, w)
			if C != t[2]:
				all_correct_class = False
				mult = 1
				if C == 1:
					mult = -1
				for i in range(2):
					w[i] += mult*t[i]
				w[2] += mult*1
	for t in data_test:
		t[2] = pone_classify(t, w)
	return 0


def pone_classify(t, w):
	dot = 0
	for i in range(2):
		dot += t[i] * w[i]
	dot += w[2]
	if dot < 0:
		return 0
	return 1


def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in index 0 and Y in index 1, and a blank space in index 2
	# to be filled with class
	# The class value could be a 0 or a 9
	w = [[0 for i in range(3)] for j in range(10)]

	all_correct_class = False
	while not all_correct_class:
		all_correct_class = True
		for t in data_train:
			C = ptwo_classify(t, w)
			if C != t[2]:
				all_correct_class = False
				for i in range(3):
					w[C][i] -= t[i]
					w[int(t[2])][i] += t[i]
	for t in data_test:
		t[2] = ptwo_classify(t, w)
	return 0


def ptwo_classify(t, weights):
	class_ret = 0
	dot_max = -100000
	for num, w in enumerate(weights):
		dot = 0
		for i in range(2):
			dot += t[i] * w[i]
		dot += w[2]
		if dot > dot_max:
			dot_max = dot
			class_ret = num
	return class_ret

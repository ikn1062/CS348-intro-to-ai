import common
import math


def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(height, width)"
	vote_space = common.init_space(2001, 2001)

	for y in range(len(image)):
		for x in range(len(image[0])):
			if image[y][x] == 0:
				for m in range(-1000, 1000):
					b = y - (m * 0.01) * x
					if (b >= -1000) and (b <= 1000):
						b = b + 1000
						m = m + 1000
						vote_space[int(round(m))][int(round(b))] += 1
	max_vote = 0
	line = common.Line()
	for m in range(len(vote_space)):
		for b in range(len(vote_space[0])):
			if vote_space[m][b] > max_vote:
				max_vote = vote_space[m][b]
				line.m = (m - 1000) * 0.01
				line.b = b - 1000
	return line


def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	vote_space = common.init_space(200, 200)
	r = 30
	thresh = 200

	for y in range(len(image)):
		for x in range(len(image[0])):
			if image[y][x] != 255:
				for theta in range(360):
					theta_rad = math.radians(theta)
					b = y - (r*math.sin(theta_rad))
					a = x - (r*math.cos(theta_rad))
					if (a >= 0) and (b >= 0) and (a <= 199) and (b <= 199):
						vote_space[int(a)][int(b)] += 1
	num_circles = 0
	for i in range(len(vote_space)):
		for j in range(len(vote_space[0])):
			if vote_space[i][j] > thresh:
				num_circles += 1
	return num_circles

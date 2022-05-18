def order(data):
	"""
	Lab 0 Sorting function - Ishaan Narain (ikn1062)
	The function utilizes mergesort algorithm to sort the input array
	:param data: Input array to be sorted
	:return: Sorted array
	"""
	# Base case:
	if len(data) <= 1:
		return data

	# Split the data array into left and right
	mid_point = len(data)//2
	left_data = data[:mid_point]
	right_data = data[mid_point:]

	# Recursively call order (or mergesort) on left and right data arrays
	order(left_data)
	order(right_data)

	# Merge and sort the left and right data arrays
	merge_sorted_data = merge(left_data, right_data, data)

	return merge_sorted_data


def merge(left, right, out):
	"""
	Merge Helper function
	Goes through all elements of the array in both left & right arrays and sorts and merges values
	:param out: Output array
	:param left: Left array to be merged and sorted
	:param right: Right array to be merged and sorted
	:return: Merge sorted array
	"""
	i = 0
	j = 0
	k = 0

	while len(left) > i and len(right) > j:
		if left[i] > right[j]:
			out[k] = right[j]
			j += 1
		else:
			out[k] = left[i]
			i += 1
		k += 1

	if len(left) > i:
		while len(left) > i:
			out[k] = left[i]
			i += 1
			k += 1

	if len(right) > j:
		while len(right) > j:
			out[k] = right[j]
			j += 1
			k += 1
	return out

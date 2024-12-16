import numpy as np

with open("input", 'r') as dfh:

	binary_array = np.array([])

	str_binary_list = list(map(lambda x: x.strip(), dfh.readlines()))

	binary_list = [list(map(lambda x: int(x), [*x])) for x in str_binary_list]

	binary_array = np.array(binary_list)

	column_count = binary_array.shape[1]

	# For O2
	for j in range(0, column_count):
		zero, one = np.bincount(binary_array[:, j])

		if zero != one:
			most_common_bit = np.bincount(binary_array[:, j]).argmax()
			binary_array = binary_array[ binary_array[:, j] == most_common_bit ]
		elif zero == one:
			binary_array = binary_array[ binary_array[:, j] == 1 ]

			if binary_array.shape[0] == 1:
				bit = ''
				for k in binary_array[0]:
					bit += str(k)
				oxygen_generator_rating = int(bit, 2)
				break

	binary_array = np.array(binary_list)

	for j in range(0, column_count):
		zero, one = np.bincount(binary_array[:, j])

		if zero != one:
			least_common_bit = np.bincount(binary_array[:, j]).argmin()
			binary_array = binary_array[ binary_array[:, j] == least_common_bit ]
		elif zero == one:
			binary_array = binary_array[ binary_array[:, j] == 0 ]
			if binary_array.shape[0] == 1:
				bit = ''
				for k in binary_array[0]:
					bit += str(k)
				co2_generator_rating = int(bit, 2)
				break

	life_supporting_rating = oxygen_generator_rating * co2_generator_rating

	print(f'The life support rating of the sumarine is : {life_supporting_rating} !!')

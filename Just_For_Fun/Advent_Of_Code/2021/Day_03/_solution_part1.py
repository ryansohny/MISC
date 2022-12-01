import numpy as np

with open("input", 'r') as dfh:

        binary_array = np.array([])

        str_binary_list = list(map(lambda x: x.strip(), dfh.readlines()))

        binary_list = [list(map(lambda x: int(x), [*x])) for x in str_binary_list]

        binary_array = np.array(binary_list)

        column_count = binary_array.shape[1]

#       np.bincount(a[:, 1]).argmax()

        most_common_bits = ''
        least_common_bits = ''

        for j in range(0, column_count):

                most_common_bits += str(np.bincount(binary_array[:, j]).argmax())

                least_common_bits += str(np.bincount(binary_array[:, j]).argmin())

        most_common_bits = int(most_common_bits, 2)
        least_common_bits = int(least_common_bits, 2)

        power_consumption = most_common_bits * least_common_bits

        print(f'The epsilon rate is : {most_common_bits} !!')
        print(f'The epsilon rate is : {least_common_bits} !!')

        print(f'The power consumption of the sumarine is : {power_consumption} !!')

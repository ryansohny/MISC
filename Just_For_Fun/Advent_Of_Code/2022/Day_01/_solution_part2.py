# Find the Elf carrying the most Calories, How many total Calories is that Elf carrying?

import numpy as np

with open("input", 'r') as dfh:
        items_list = list(map(lambda x: int(x.strip('\n')) if x.strip('\n') != '' else x.strip('\n'), dfh.readlines()))
        indices = [i for i,x in enumerate(items_list) if x == '']

        start = 0
        calories_list = []

        for i in indices:
                calories = np.sum(items_list[start: i])

                calories_list.append(calories)

                start = i + 1

        # The Last Elf's Calories
        calories = np.sum(items_list[start: len(items_list)])
        calories_list.append(calories)

        print(np.sum(sorted(calories_list)[::-1][:3]))

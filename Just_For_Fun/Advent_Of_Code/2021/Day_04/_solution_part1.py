import numpy as np

input_path = "C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Advent_Of_Code\\2021\\Day_04\\"

with open(f"{input_path}input", 'r') as dfh:
    draw = list(map(lambda x: int(x), dfh.readline().strip().split(',')))
    dfh.readline() # empty line
    boards = list(map(lambda x: x.strip(), dfh.readlines()))
    delimiter_indices = [i for i, x in enumerate(boards) if x == '']
    
    boards_array_list = []
    start = 0
    for i in delimiter_indices:
        boards_array = np.array( list(map(lambda x: list(map(lambda y: int(y), x.split())), boards[start: i])) )
        boards_array_list.append(boards_array)
        start = i + 1
    
    boards_array = np.array( list(map(lambda x: list(map(lambda y: int(y), x.split())), boards[start:])) ) # The last one
    boards_array_list.append(boards_array)
    
    
        
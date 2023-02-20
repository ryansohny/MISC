input_path = "C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Advent_Of_Code\\2022\\Day_03\\"

import string
import difflib

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priorities = dict(zip(alphabet, list(range(1, len(alphabet)+1))))
sum_priorities = 0

with open(f"{input_path}input", 'r') as dfh:
    for line in dfh:
        line = line.strip()
        first_compartment = line[0:int(len(line)/2)]
        second_compartment = line[int(len(line)/2):]
        match = difflib.SequenceMatcher(None, first_compartment, second_compartment)
        overlapped = first_compartment[match.find_longest_match(0, len(first_compartment), 0, len(second_compartment))[0]]
        sum_priorities += priorities[overlapped]       
    print(sum_priorities)
        
            
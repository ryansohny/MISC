input_path = "C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Advent_Of_Code\\2022\\Day_03\\"

import string
import difflib

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priorities = dict(zip(alphabet, list(range(1, len(alphabet)+1))))
sum_priorities = 0

with open(f"{input_path}input", 'r') as dfh:
    rucksack = dfh.readlines()
    for i in range(0, int(len(rucksack)/3)):
        a = list(rucksack[3*i].strip())
        b = list(rucksack[3*i+1].strip())
        c = list(rucksack[3*i+2].strip())
        overlapped = list(set(list(a)) & set(list(b)) & set(list(c)))[0]
        sum_priorities += priorities[overlapped]
    print(sum_priorities)
import sys
import re

digit_character = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
digit = tuple(i for i in range(1,10))

char_digit_dict = dict(zip(digit_character, digit))

def digit_index_extractor(string):
    index_list = list()
    for i, s in enumerate(string):
        if s.isdigit():
            index_list.append(i)
    return index_list # empty list if no digit

def chardigit_index_extractor(string, substring):
    index_list = list()
    return [index.start() for index in re.finditer(re.escape(substring), string)]

def total_index_extractor(string) -> list:
    template_dict = dict()
    template_dict['digit'] = digit_index_extractor(string)
    for i in char_digit_dict:
        template_dict[i] = chardigit_index_extractor(string, i)
    
    for k in list(template_dict.keys()):
        if template_dict[k] == []:
            del template_dict[k]
    
    value_list = list()
    for l in template_dict.values():
        value_list.extend(l)

    digit_list = list()
    for k in template_dict:
        if k == 'digit':
            for v in template_dict[k]:
                digit_list.append(string[v])
        else:
            for v in template_dict[k]:
                digit_list.append(char_digit_dict[k])
    return sorted(dict(zip(value_list, digit_list)).items())

def main():
    input = "/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Advent_Of_Code/2023/input"
    with open(input, 'r') as dfh:
        calibration_values = list()
        for i in dfh:
            calibration_values.append(int(str(total_index_extractor(i)[0][1]) + str(total_index_extractor(i)[-1][1])))
        print(f'The Sum of the Calibration values: {sum(calibration_values)}')

if __name__ == "__main__":
    main()

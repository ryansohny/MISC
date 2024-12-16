import sys

def calibration_value_extractor(string):
    string = string.strip()
    calibration_value = ''
    for i in string:
        if i.isdigit():
            calibration_value += i
            break
    for i in string[::-1]:
        if i.isdigit():
            calibration_value += i
            break
    return int(calibration_value)

def main():
    input = "/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Advent_Of_Code/2023/input"
    with open(input, 'r') as dfh:
        calibration_values = list()
        line = list(map(lambda x: x.strip(), dfh.readlines()))
        for i in line:
            calibration_values.append(calibration_value_extractor(i))
        print(f'The Sum of the Calibration values: {sum(calibration_values)}')
if __name__ == "__main__":
    main()
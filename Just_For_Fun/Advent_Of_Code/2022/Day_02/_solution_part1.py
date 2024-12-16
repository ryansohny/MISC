#A X
#A Z
# A: Rock, B: Paper, C: Scissor
# X: Rock, Y: Paper, Z: Scissor
#import os
#print(os.getcwd())

def score_calculator(List):
    if List[0] == 'A':
        if List[1] == 'X':
            return 1 + 3
        elif List[1] == 'Y':
            return 2 + 6
        else:
            return 3 + 0
    elif List[0] == 'B':
        if List[1] == 'X':
            return 1 + 0
        elif List[1] == 'Y':
            return 2 + 3
        else:
            return 3 + 6
    else:
        if List[1] == 'X':
            return 1 + 6
        elif List[1] == 'Y':
            return 2 + 0
        else:
            return 3 + 3


input_path = "C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Advent_Of_Code\\2022\\Day_02\\"

with open(f"{input_path}input", 'r') as dfh:
    total_score = 0
    for i in dfh:
        game = i.strip().split()
        total_score += score_calculator(game)
    print(total_score)
    
# 8890
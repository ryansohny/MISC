#A X
#A Z
# A: Rock, B: Paper, C: Scissor
# X: Rock, Y: Paper, Z: Scissor

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
        
with open("input", 'r') as dfh:
    total_score = 0
    for i in dfh:
        game = i.strip().split()
        total_score += score_calculator(game)
    print(total_score)
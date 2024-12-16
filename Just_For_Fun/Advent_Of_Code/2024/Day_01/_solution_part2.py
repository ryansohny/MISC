def main():
    input = "/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Advent_Of_Code/2024/input"
    with open(input, 'r') as dfh:
        left, right = list(), dict()
        sim_score = 0
        for i in dfh:
            line = i.strip().split()
            left.append(int(line[0]))
            try:
                right[int(line[1])] += 1
            except KeyError:
                right[int(line[1])] = 1
        
        for i in left:
            try:
                sim_score += (i * right[i])
            except KeyError:
                pass

        print(sim_score)
if __name__ == "__main__":
    main()
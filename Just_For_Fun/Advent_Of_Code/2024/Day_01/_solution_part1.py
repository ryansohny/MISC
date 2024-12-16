def main():
    input = "/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Advent_Of_Code/2024/input"
    with open(input, 'r') as dfh:
        right, left = list(), list()
        sum = 0
        for i in dfh:
            line = i.strip().split()
            right.append(int(line[0]))
            left.append(int(line[1]))
        right = sorted(right)
        left = sorted(left)
        
        for i in range(len(right)):
            sum += abs(right[i] - left[i])

        print(sum)
if __name__ == "__main__":
    main()
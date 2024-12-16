def main():
    input = "/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Advent_Of_Code/2024/Day_02/input"
    with open(input, 'r') as dfh:
        safe = 0
        for i in dfh:
            levels  = list(map(lambda x: int(x), i.strip().split()))
            levels_change = [levels[j+1]-levels[j] for j in range(len(levels)-1)]
            if all(0 < abs(x) <= 3 for x in levels_change):
                if sum([abs(k) for k in levels_change]) == abs(sum(levels_change)):
                    safe += 1
    print(safe)
if __name__ == "__main__":
    main()


input_path = "C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Advent_Of_Code\\2022\\Day_04\\"

with open(f"{input_path}input", 'r') as dfh:    
    overlap = 0
    for line in dfh:
        line = line.strip().split(',')
       
        # Numerical Method
        first_range = list(map(lambda x: int(x), line[0].split('-')))        
        second_range = list(map(lambda x: int(x), line[1].split('-')))

        if first_range[0] <= second_range[0] and first_range[1] >= second_range[0]:
            overlap += 1
        elif second_range[0] <= first_range[0] and second_range[1] >= first_range[0]:
            overlap += 1
       # List method    
#        first_range = list(range(first_range[0], first_range[1]+1))
#        second_range = list(range(second_range[0], second_range[1]+1))
#        if len(set(first_range) & set(second_range)) > 0:
#            overlap += 1
   
    print(overlap)
    

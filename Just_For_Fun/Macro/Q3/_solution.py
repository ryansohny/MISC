import os
os.chdir("C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Macro\\Q3")
os.chdir("/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Macro/Q3") # mac

with open("ascii33.txt", 'r') as asciif:
    ascii33_dict = {}
    for q, a in enumerate(asciif.readline().strip()):
        ascii33_dict[a] = q # Phred Quality Score
    
with open("sample_1.fastq", 'r') as fastq:
    c = 0
    total_read_count = 0
    base_count = dict(zip(['A', 'T', 'G', 'C', 'N'], [0]*5))
    q20 = 0
    q30 = 0
    for line in fastq:
        c += 1
        if c % 4 == 2:
            total_read_count += 1
            line = line.strip()
            # base count
            base_count['A'] += line.count('A')
            base_count['T'] += line.count('T')
            base_count['G'] += line.count('G')
            base_count['C'] += line.count('C')
            base_count['N'] += line.count('N')
        elif c % 4 == 0:
            line = line.strip()
            for base in line:
                if ascii33_dict[base] >= 20:
                    q20 += 1
                    if ascii33_dict[base] >= 30:
                        q30 += 1
    
    print(f'Total Read Count: {total_read_count}')
    print(f'Total Base Count: {sum(base_count.values())}')
    print(f'Total A Count: {base_count["A"]}')
    print(f'Total C Count: {base_count["C"]}')
    print(f'Total G Count: {base_count["G"]}')
    print(f'Total T Count: {base_count["T"]}')
    print(f'Total N Count: {base_count["N"]}')
    print(f'Q20 Bases: {q20} ({round((q20/sum(base_count.values()))*100, 2)}%)')
    print(f'Q30 Bases: {q30} ({round((q30/sum(base_count.values()))*100, 2)}%)')
    print(f'GC Ratio: {round(((base_count["G"] + base_count["C"]) / sum(base_count.values())) * 100, 2)}%')
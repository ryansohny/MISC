import os
os.chdir("C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Macro\\Q3")

with open("sample_1.fastq", 'r') as fastq:
    c = 0
    total_read_count = 0
    for line in fastq:
        c += 1
        if c % 4 == 2:
            


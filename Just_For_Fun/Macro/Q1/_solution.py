import os
os.chdir("C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Macro\\Q1")
print(os.getcwd())

with open("gene_list.txt", 'r') as genef:
    print(genef.readline())
#import os
#print(os.getcwd())
    
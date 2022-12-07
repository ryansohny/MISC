import os
os.chdir("C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Macro\\Q1")

with open("gene_list.txt", 'r') as genef:
    exp_dic = {}
    for i in genef:
        exp_dic[i.strip()] = 'NA'

with open("expression_table.txt") as dfh:
    dfh.readline()
    for i in dfh:
        line = i.strip().split()
        try:
            exp_dic[line[0]] += float(line[2])
        except TypeError:
            exp_dic[line[0]] = float(line[2])

    for k, v in exp_dic.items():
        print(k, '\t', v)
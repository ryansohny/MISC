import pandas as pd

with open("sample.txt", 'r') as dfh, open("Sex_Determination_by_coverage.tab", 'w') as rfh:
        rfh.write("ID\ttotal_coverage\tchrX_coverage\tchrY_coverage\tchrX_coverage/total_coverage\tchrY_coverage/total_coverage\tratio_chrX/chrY\tSex_Determination_Based_on_Coverage\n")
        rfh.flush()
        for i in dfh:
                sampleid = i.strip()
                table = pd.read_table(f'{sampleid}/{sampleid}.mosdepth.summary.txt', index_col=0)
                total = round(table.loc['total']['mean'], 3)
                chrx = round(table.loc['chrX']['mean'], 3)
                chry = round(table.loc['chrY']['mean'], 3)
                if chrx/chry > 5: # set to arbitrary value (Definitely need more sophiscated value I guess?)
                        sex = 'Female'
                else:
                        sex = 'Male'
                rfh.write(f"{sampleid}\t{total}\t{chrx}\t{chry}\t{round(chrx/total, 3)}\t{round(chry/total, 3)}\t{round(chrx/chry, 3)}\t{sex}\n")
                rfh.flush()

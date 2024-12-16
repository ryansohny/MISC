import os
os.chdir("C:\\Users\\mhryansohn.MACROGEN\\Desktop\\GitHub_repo\\MISC\\Just_For_Fun\\Macro\\Q2")
os.chdir("/Users/mhryansohn/Desktop/99.Miscellaneous/GitHub_Repo/MISC/Just_For_Fun/Macro/Q2") # mac

with open("GroupA.txt", 'r') as af, open('GroupB.txt', 'r') as bf, open('GroupC.txt', 'r') as cf:
    a = list(map(lambda x: x.strip(), af.readlines()))
    b = list(map(lambda x: x.strip(), bf.readlines()))
    c = list(map(lambda x: x.strip(), cf.readlines()))
    
    print(f'Only A: {", ".join(sorted(set(a) - (set(b) | set(c))))}')
    print(f'Only B: {", ".join(sorted(set(b) - (set(a) | set(c))))}')
    print(f'Only C: {", ".join(sorted(set(c) - (set(a) | set(b))))}')
    print(f'A&B: {", ".join(sorted(set(a) & set(b)))}')
    print(f'A&C: {", ".join(sorted(set(a) & set(c)))}')
    print(f'B&C: {", ".join(sorted(set(b) & set(c)))}')
    print(f'A&B&C: {", ".join(sorted(set(a) & set(b) & set(c)))}')
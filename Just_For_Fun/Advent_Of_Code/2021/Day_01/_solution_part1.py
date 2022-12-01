with open("input", 'r') as dfh:
    first_measure = int(dfh.readline().strip('\n'))
    increase = 0

    for m in dfh:
            if first_measure < int(m.strip()):
                    increase += 1
                    first_measure = int(m.strip())
    print(increase)

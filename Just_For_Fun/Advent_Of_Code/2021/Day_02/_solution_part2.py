horizontal = 0
aim = 0
depth = 0

with open("input", 'r') as dfh:
        for course in dfh:
                course = course.strip().split()
                if course[0] == 'forward':
                        horizontal += int(course[1])
                        depth += int(course[1]) * aim
                elif course[0] == 'down':
                        aim += int(course[1])
                elif course[0] == 'up':
                        aim -= int(course[1])

        print(horizontal * depth)

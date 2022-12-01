horizontal = 0
depth = 0
with open("input", 'r') as dfh:
        for course in dfh:
                course = course.strip().split()
                if course[0] == 'forward':
                        horizontal += int(course[1])
                elif course[0] == 'down':
                        depth += int(course[1])
                elif course[0] == 'up':
                        depth -= int(course[1])

        print(horizontal * depth)

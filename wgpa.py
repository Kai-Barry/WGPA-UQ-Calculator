import numpy as np

file = open("summary.txt","r")
lines = file.readlines()
courses =[]
for i, line in enumerate(lines):
    course = ""
    courseCount = 0
    findPoint = 2
    gpa = 99
    print(line)
    if not line[0] == ' ':
        for j, letter in enumerate(line):
            if letter.isnumeric():
                if courseCount <= 3:
                    course += letter
                    courseCount += 1
                elif len(line) >= j + 1 and line[j - 1] == " " and line[j + 1] == " ":
                    gpa = int(letter)
        if not course == "" and len(course) == 4 and gpa <= 7:
            courses.append([int(course[0]), gpa, course])

print(courses)
top = 0
bottom = 0
basic = 0
for x, y, z in courses:
    basic += y
    top += x * y
    bottom += x
print("WGPA:", top/bottom)
print("GPA:", basic/len(courses))

# tee ratkaisu tänne
def grades_conversion(score,point):
    result = 0
    value = (score // 4) + point
    if value > 27 :
        result = 5
    elif value > 23:
        result = 4
    elif value > 20:
        result = 3
    elif value > 17:
        result = 2
    elif value > 14:
        result = 1
    return result, score//4, value

names = {}
grades = {}
exam = {}
course = []

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_point = input("Exams points: ")
    course_text = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_point = "exam_points1.csv"
    course_text = "course1.txt"

with open(student_info) as student_file,open(exercise_data) as exercise_file,open(exam_point) as exam_file,open(course_text) as course_file:
    for line in student_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] +" "+ parts[2]

    for line in exercise_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        grades[parts[0]] = 0
        for i in range(1,len(parts)):
            grades[parts[0]] += int(parts[i])

    for line in exam_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exam[parts[0]] = 0
        for i in range(1,len(parts)):
            exam[parts[0]] += int(parts[i])

    for line in course_file:
        parts = line.replace("\n","")
        part = parts.split(":")
        course.append(part[1])

text = "name"
title = "exec_nbr"
word = "exec_pts."
strings = "exm_pts."
phrase = "tot_pts."
caption = "grade"

blank =""

text_file = "results.txt"
csv_file = "results.csv"

with open(text_file,"w") as result_text,open(csv_file,"w") as result:
    for space in course:
        blank += space[1:] + ", "
    blank = blank[:-2] + " credits"
    char = "="*len(blank)
    result_text.write(blank+"\n")
    result_text.write(char+"\n")
    result_text.write(f"{text:30}{title:10}{word:10}{strings:10}{phrase:10}{caption:10}\n")
    for id, name in names.items():
        if id in grades:
            score,exercise,total = grades_conversion(grades[id],exam[id])
            result_text.write(f"{names[id]:30}{grades[id]:<10}{exercise:<10}{exam[id]:<10}{total:<10}{score:<10}\n")
            result.write(f"{id};{names[id]};{score}\n")

print(f"Results written to files {text_file} and {csv_file}")
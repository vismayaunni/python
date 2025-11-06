python_students = {"Asha", "John", "Priya"}
data_science_students = {"Priya", "Vikram", "Sam"}
python_students.add("Sara")
data_science_students.remove("Sam")
both_courses = python_students & data_science_students
print(both_courses)
only_python = python_students - data_science_students
print(only_python)
all_students = python_students | data_science_students
print(all_students)
course_dict = {"Python": len(python_students), "Data Science": len(data_science_students)}
for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")
growth_dict = {course: count * 2 for course, count in course_dict.items()}
print(growth_dict)
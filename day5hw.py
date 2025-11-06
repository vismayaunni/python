frontend_students = {"Asha", "John", "Priya"}
backend_students = {"Priya", "Vikram", "Sam"}
backend_students.add("Sara")
frontend_students.remove("John")
both_courses = frontend_students & backend_students
print(both_courses)
only_backend = backend_students - frontend_students
print(only_backend)
total_unique = len(frontend_students | backend_students)
print(total_unique)
course_dict = {"Frontend": len(frontend_students), "Backend": len(backend_students)}
for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")
fullstack_dict = {**course_dict, "Fullstack": len(frontend_students) + len(backend_students)}
print(fullstack_dict)
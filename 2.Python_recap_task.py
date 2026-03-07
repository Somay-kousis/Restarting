# Data Processing Tool


# load JSON
# → manipulate data
# → filter records
# → compute statistics
# → call an API
# → merge data
# → save results

import json 

students = [
    {"name": "Aman", "age": 21, "marks": 88, "city": "Delhi"},
    {"name": "Sara", "age": 20, "marks": 72, "city": "Mumbai"},
    {"name": "Rohit", "age": 22, "marks": 91, "city": "Pune"},
    {"name": "Neha", "age": 19, "marks": 65, "city": "Delhi"},
]

with open ("student.json", "w") as f:
    json.dump(students, f, indent=4)

with open ("student.json", "r") as f:
    students = json.load(f)

for student in students:
    print(student["name"])

for student in students:
    if student["marks"] > 80:
        print(student)

names = [s["name"] for s in students]
print(names)

marks = [s["marks"] for s in students]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
city = input("Enter city: ")

new_student = {
    "name": name,
    "age": age,
    "marks": marks,
    "city": city
}

students.append(new_student)

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

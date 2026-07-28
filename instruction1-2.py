student_grades = {
    "Amara": [92, 88, 95],
    "Leo": [70, 65, 80]
}

favorite_subjects = {}

def add_student(data, name, info):
    data[name] = info

def get_average(data):
    averages = {}

    for name, scores in data.items():
        averages[name] = sum(scores) / len(scores)

    return averages

add_student(favorite_subjects, "Amara", {"Math", "Science", "Geometry"})
add_student(favorite_subjects, "Leo", {"PE", "Geology", "AI"})
add_student(favorite_subjects, "John", {"Physics", "History", "PE"})
add_student(favorite_subjects, "Jacob", {"Foodtech", "ML", "Java"})

add_student(student_grades, "John", [85, 90, 78])
add_student(student_grades, "Jacob", [60, 55, 70])

average_scores = get_average(student_grades)

average_scores = get_average(student_grades)

print(average_scores)
print(favorite_subjects)

passed = {
    name: average
    for name, average in average_scores.items()
    if average > 80
}

print(passed)
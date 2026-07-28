def add_student(subjects, name, favorite_subjects):
    subjects[name] = favorite_subjects

roster = {
    "Amara": [92, 88, 95],
    "Leo": [70, 65, 80]
}

subjects = {}

add_student(subjects, "Amara", {"Geometry", "Math", "Science"})
add_student(subjects, "Leo", {"PE", "Geology", "AI"})
add_student(subjects, "John", {"Physics", "History", "PE"})
add_student(subjects, "Jacob", {"Foodtech", "ML", "Java"})

def get_average(scores):
    return sum(scores) / len(scores)

averages = {
    name: get_average(scores)
    for name, scores in roster.items()
}

top_students = {
    name: average
    for name, average in averages.items()
    if average > 80
}

print(averages)
print(subjects)
print(top_students)

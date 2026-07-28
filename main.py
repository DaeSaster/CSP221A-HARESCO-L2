def save_entry(mapping, key, payload):
    mapping[key] = payload

def compute_averages(data_map):
    return {
        student: sum(scores) / len(scores) 
        for student, scores in data_map.items()
    }

grades = {
    "Amara": [92, 88, 95],
    "Leo": [70, 65, 80]
}

save_entry(grades, "John", [85, 90, 88])
save_entry(grades, "Jacob", [78, 82, 80])

favorite_subjects = {}
save_entry(favorite_subjects, "Amara", {"Math", "Science", "Geometry"})
save_entry(favorite_subjects, "Leo", {"AI", "Geology", "PE"})
save_entry(favorite_subjects, "John", {"Physics", "History", "PE"})
save_entry(favorite_subjects, "Jacob", {"Java", "ML", "Foodtech"})

averages = compute_averages(grades)
passed = {name: avg for name, avg in averages.items() if avg > 80}

print("Average Grades:")
print(averages)

print("\nFavorite Subjects:")
print(favorite_subjects)

print("\nStudents with Average Above 80:")
print(passed)
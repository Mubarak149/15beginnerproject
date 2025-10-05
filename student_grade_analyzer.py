students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append({"name":name, "score":grade})

scores = []
for student in students:
    score = student["score"]
    scores.append(score)

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

for student in students:
    if student["score"] == highest_score:
        print(f"Top Student: {student['name']} with score {student['score']}")
    if student["score"] == lowest_score:
        print(f"Lowest Student: {student['name']} with score {student['score']}")
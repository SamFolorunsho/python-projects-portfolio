students = []


def grade_for_score(score):
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:
        return "C"
    if score >= 40:
        return "D"
    if score >= 30:
        return "E"
    return "F"


while True:
    name = input("What's the student's name? ")
    if not name.strip():
        break

    scores = input("Enter the student's scores separated by spaces: ")
    scores_list = [float(score) for score in scores.split()]
    students.append(
        {"name": name.strip(), "scores": scores_list, "total_score": sum(scores_list)}
    )

print("\nStudent records:")
students.sort(key=lambda student: student["total_score"], reverse=True)

for rank, student in enumerate(students, start=1):
    if 10 <= rank % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(rank % 10, "th")
    print(
        f"{rank}{suffix}. {student['name']}  {student['total_score']:g} " f"{grade_for_score(student['total_score'])} ",
    )
 

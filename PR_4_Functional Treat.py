#  (que 1)Data input & initialization

marks = [35, 40, 98, 75, 67, 76, 42, 25, 92,89,
         78, 45, 23, 65, 56, 89, 90, 37, 100, 66]

# (que 2)Basic analysis (Built in function)

total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average = sum(marks) / total_students



passed_students = len([a for a in marks if a >=40 ])
failed_students = len([a for a in marks if a < 40])
exact_100 = marks.count(100)
pass_percentage = (passed_students / total_students) * 100


print("total students:", total_students)
print("highest marks:",highest_marks)
print("lowest marks:",lowest_marks)
print("average:",average)
print("passed students:",passed_students)
print("failed students:", failed_students)
print("exactly 100:",exact_100)
print("pass percentage:",pass_percentage, "%")

print()

# (que 3) advanced built in function

ascending = sorted(marks)
descending = sorted(marks, reverse = True)

print("sorted ascending:",ascending)

print("sorted descending(reverse):", descending)

print("second highest:", marks[-2])

print("second lowest:", marks[1])

print()

print(" All passed :", all(a >=40 for a in marks))

print(" Any failed:",any(a < 40 for a in marks))

print()

# que 4 optional (IF time permits )

b = int(input("enter a mark to check:"))

if b in marks:
    print(b, "is in the list.")

else:
    print(b, "is not in the list.")

print()

# que 5 Bonus Task 

grades = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}

for a in marks:
    if a >= 90:
        grades["A"] += 1

    elif a>= 80:
        grades["B"] += 1
    
    elif a >= 70:
        grades["C"] += 1
    
    elif a >= 60:
        grades["D"] += 1
    
    elif a >= 40:
        grades["E"] += 1

    else:
        grades["F"] += 1


for grades,count in grades.items():
    print(f"Grade {grades}:{count}students")
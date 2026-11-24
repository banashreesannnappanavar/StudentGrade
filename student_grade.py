name = input("Enter Student Name: ")
dept = input("Enter Department: ")
sem = input("Enter Semester: ")

m1 = float(input("Enter Subject 1 Marks: "))
m2 = float(input("Enter Subject 2 Marks: "))
m3 = float(input("Enter Subject 3 Marks: "))

avg = (m1 + m2 + m3) / 3

if avg >= 90:
    grade = "S"
elif avg >= 80:
    grade = "A"
elif avg >= 65:
    grade = "B"
elif avg >= 50:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "F"

print("\nStudent Details")
print("Name:", name)
print("Department:", dept)
print("Semester:", sem)
print("Average:", round(avg, 2))
print("Grade:", grade)
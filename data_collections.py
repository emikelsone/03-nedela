numbers = [1, 2, 3, 4, 5, 6]
numbers.append(6)
numbers.pop()

total=0
for num in numbers:
    total += num
print("Total:", total)

count=0
for num in numbers:
    count += 1
print("Count:", count)

average = total / count
print("Average:", average)

even_numbers = []
for num in numbers:
    if num % 2 == 0: # parbauda, vai skaitlis ir pāra skaitlis. Ja num % 2 ir vienāds ar 0, tas nozīmē, ka num ir pāra skaitlis.
        even_numbers.append(num)
print("Even numbers:", even_numbers)

print("\n ---Saraksti ---") #slice demonstracija
print("Pirmie trīs skaitļi:", numbers[0:3])
print("Pēdējie trīs skaitļi:", numbers[-3:])
print("Skaitļi no indeksa 2 līdz 4:", numbers[2:5])

students = {"Anna": 85, "Jānis": 72, "Līga": 95, "Pēteris": 68, "Zane": 90, "Mārtiņš": 78}
print("\n ---Vārdnīcas ---")

#lai nevajadzetu rakstīt katru vārdu un vērtību atsevišķi, var izmantot ciklu, lai izdrukātu visus vārdus un vērtības vārdnīcā.
for name, grade in students.items():
    print(name, ":", grade)

best_student = max(students, key=students.get)
print("Labākais students:", best_student, "ar atzīmi", students[best_student])


print("\n ---Studenti ar atzīmi >= 80 ---")

students_list = [
{"name": "Anna", "grade": 85},
{"name": "Jānis", "grade": 72}, 
{"name": "Līga", "grade": 95}, 
{"name": "Pēteris", "grade": 68}, 
{"name": "Zane", "grade": 90}, 
{"name": "Mārtiņš", "grade": 78}
]


good_students = []
for student in students_list:
    if student["grade"] >= 80:
        good_students.append(student)

for i, student in enumerate(good_students, start=1):
    print(f"{i}. {student['name']} - {student['grade']}")



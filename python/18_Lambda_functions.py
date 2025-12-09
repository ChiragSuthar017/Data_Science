print("Lambda functions")

cube = lambda a:a*a*a
cube(3)

s = lambda a,b : a+b
s(4,6)

print("Lambda in Sorting Functions")

students = [("Alice", 85), ("Bob", 78), ("Charlie", 92)]
students.sort(key=lambda student: student[1])  # Sort by score
print(students)  # Output: [('Bob', 78), ('Alice', 85), ('Charlie', 92)]
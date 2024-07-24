student_heights = [151, 145, 179]

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum = 0
count = 0
for student_height in student_heights:
    sum += student_height
    count += 1

average = sum / count
print(f"total height = {sum}\nnumber of students = {count}\naverage height = {round(average)}")

# EXPECTED OUTPUT

# total height = 1146
# number of students = 7
# average height = 164
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

student_num = 0
height_sum = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    student_num += 1
    height_sum += student_heights[n]

print(round(height_sum / student_num))

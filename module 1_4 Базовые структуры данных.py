grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = list(["Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"])
students = sorted (students)
students1 = sum(grades[0]) / len(grades [0])
students2 = sum(grades [1]) / len(grades [1])
students3 = sum(grades [2]) / len(grades [2])
students4 = sum(grades[3])/ len(grades [3])
students5 = sum(grades [4]) / len(grades [4])
result = {students[0]:students1, students [1]: students2, students[2]: students3, students[3]:students4, students[4]:students5}
print(result)
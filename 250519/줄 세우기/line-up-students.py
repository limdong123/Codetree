n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class Student:
    def __init__(self, height, weight, index):
        self.h = height
        self.w = weight
        self.idx = index

students_data = []
for i in range(n):
    students_data.append(students[i][0], students[i][1], students[i][2])

students_data.sort(key = lambda x : (-x.h, -x.w, x.idx))
for i in range(n):
    print(f"{students_data[i][0]} {students_data[i][1]} {students_data[i][2]}")
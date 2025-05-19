n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class Student:
    def __init__(self, h, w, idx):
        self.h = h
        self.w = w
        self.idx = idx

students_class = []
for i in range(n):
    students_class.append(Student(students[i][0], students[i][1], students[i][2]))

students_class.sort(key = lambda x : (x.h, -x.w))
for i in range(n):
    print(f"{students_class[i].h} {students_class[i].w} {students_class[i].idx}")

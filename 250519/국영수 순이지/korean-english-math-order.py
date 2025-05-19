n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Score:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.kor =  korean
        self.eng = english
        self.math = math

scores = []
for i in range(n):
    scores.append(Score(name[i], korean[i], english[i], math[i]))

scores.sort(key = lambda x : (-x.kor, -x.eng, -x.math))
for i in range(n):
    print(f"{scores[i].name} {scores[i].kor} {scores[i].eng} {scores[i].math}")
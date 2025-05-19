n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Score:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.sc1 = score1
        self.sc2 = score2
        self.sc3 = score3

scores = []
for i in range(n):
    scores.append(Score(name[i], score1[i], score2[i], score3[i]))

scores.sort(key = lambda x : (x.sc1 + x.sc2 + x.sc3))
for i in range(n):
    print(f"{scores[i].name} {scores[i].sc1} {scores[i].sc2} {scores[i].sc3}")
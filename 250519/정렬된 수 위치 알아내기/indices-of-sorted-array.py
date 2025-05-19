n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# 3 1 6 2 7 30 1
# 4 1 5 3 6 7 2
# 숫자를 정렬 하고 1 1 2 3 6 7 30이 인덱스 저장하고 원래 숫자에 대입
class Sequence:
    def __init__(self, idx, number):
        self.idx = idx
        self.number = number

seqs = []
seqs_2 = []
for i in range(n):
    seqs.append(Sequence(i+1, sequence[i]))
    seqs_2.append(Sequence(i+1, sequence[i]))


seqs.sort(key = lambda x : x.number)
for i in range(n):
    seqs[i].idx = i+1
#seqs_2  =  3 1 6 2 7 30 1
#seqs    =  1 1 2 3 6 7 30
for i in range(n):
    for j in range(n):
        if seqs_2[i].number == seqs[j].number:
            print(j+1, end=" ")
            seqs[j].number = -1
            break
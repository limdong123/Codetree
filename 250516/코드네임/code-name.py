MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename = "", score = 0):
        self.cn = codename
        self.sc = score

agents = []
for i in range(MAX_N):
    agents.append(Agent(codenames[i], scores[i]))

min_sc = 101
for i in range(MAX_N):
    min_sc = min(min_sc, agents[i].sc)

for i in range(MAX_N):
    if min_sc == agents[i].sc:
        print(agents[i].cn, agents[i].sc)
        break
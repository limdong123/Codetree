secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Misson:
    def __init__(self, secret_code, meeting_point, time):
        self.sc = secret_code
        self.mp = meeting_point
        self.t = time


misson1 = Misson(secret_code, meeting_point, time)
print(f"secret code : {misson1.sc}")
print(f"meeting point : {misson1.mp}")
print(f"time : {misson1.t}")

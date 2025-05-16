n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Weather:
    def __init__(self, date = "", day = "", weather = ""):
        self.date = date
        self.day = day
        self.weather = weather

weathers = []
result_idx = 0
for i  in range(n):
    weathers.append(Weather(date[i], day[i], weather[i]))
    if weathers[i].weather == "Rain":
        result_idx = i


for i in range(result_idx - 1 , -1, -1):# weather이 rain이고 가장 작은 date 구하기
    if weathers[i].weather == "Rain" and weathers[i].date < weathers[result_idx].date:
        result_idx = i

print(weathers[result_idx].date, weathers[result_idx].day, weathers[result_idx].weather)


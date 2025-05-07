y = int(input())

# Please write your code here.
def leap_year(y):
    if(y%100 == 0 and y%400!=0):
        return False
    elif(y%4 == 0):
        return True
    return False

if(leap_year(y)):
    print("true")
else:
    print("false")

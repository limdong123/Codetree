user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self,user_id = "", level = 0):
        self.user_id = user_id
        self.level = level
    
user1 = User()
user2 = User(user2_id, user2_level)

user1.user_id = "codetree"
user1.level = "10"

print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")
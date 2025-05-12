text = input()
pattern = input()

# Please write your code here.
def function():
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

result = function()
print(result)

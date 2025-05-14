word1 = input()
word2 = input()

# Please write your code here.
arr_word1 = list(word1)
arr_word1.sort()
str_word1 = ''.join(arr_word1)

arr_word2 = list(word2)
arr_word2.sort()
str_word2 = ''.join(arr_word2)

print("Yes") if str_word1 == str_word2 else print("No")
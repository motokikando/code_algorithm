s = input()

num =["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for i in range(len(s)):
    if s[i] in num:
        num.remove(s[i])

print(num[0])



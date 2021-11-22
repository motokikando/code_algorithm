
# s = 'konnitiwa'
# s = input()
# print(s[0]+str(len(s)-2)+s[-1])


#べき乗マイナス
# X = 981506241
# X = int(input())
# print(int(X**0.25))

#AroundSpace
N = int(input())
#もし0.5のべき乗をして
for i in reversed(range(N+1)):
    if (i**0.5).is_integer():
        print(i)
        break


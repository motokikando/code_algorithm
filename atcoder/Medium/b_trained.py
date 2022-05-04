N =int(input())
a_list = [int(input()) for i in range(N)]

def get_button_count(l):
    cnt = 1
    i = 1
    flag = True
    if l[i-1] == 2:
        flag = False
        return cnt
    while(flag):
        i = l[i-1]
        cnt += 1
        if l[i-1] == 2:
            flag = False
        elif cnt > 10**5:
            cnt = -1
            flag = False
    return cnt

print(get_button_count(a_list))
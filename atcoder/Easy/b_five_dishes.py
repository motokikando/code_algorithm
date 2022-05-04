
l = [int(input()) for i in range(5)]
def get_sum_time(dishes):
    q_list = [ q % 10 for q in dishes]
    ans = 0
    for i in range(len(dishes)):
        if dishes[i] % 10 == 0:
            ans += dishes[i]
        else:
            ans += dishes[i] + (10 - (dishes[i] % 10))
    q_list = [ q for q in q_list if q != 0]
    if q_list != []:
        ans -= 10 - min(q_list)
    return ans

print(get_sum_time(l))


x = 3.14
print(x.is_integer())

n = int(input())
a = []

for i in range(10):
    a.append(i*1)
    a.append(i*2)
    a.append(i*3)
    a.append(i*4)
    a.append(i*5)
    a.append(i*6)
    a.append(i*7)
    a.append(i*8)
    a.append(i*9)

if n in a:
    print('Yes')
else:
    print('No')


N=int(input())
for num in range(1,10):
    #もしNをnumで割った値が整数かつその値が1から9の値に入る時
    if (N/num).is_integer() and 1<=(N/num)<=9:
        print("Yes")
        break
else:
    print("No")
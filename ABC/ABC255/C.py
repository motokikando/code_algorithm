x,a,d,n=map(int,input().split())
z=a+d*n-d
if d<0: a,d,z=z,-d,a
c=(x-a)%d if d else 0
print([a-x,min(c,d-c),x-z][(x>a)+(x>z)])
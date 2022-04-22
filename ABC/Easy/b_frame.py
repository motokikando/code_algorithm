height, wide = map(int, input().split())
A = [input() for i in range(height)]
def draw_frame(h, w , a):
    print("#"*(w+2))
    for value in a:
        print("#" + value +"#")
    print("#"*(w+2))

draw_frame(height, wide, A)

l = [1,2, 3, 4, 5]
print(*A,sep="\n")
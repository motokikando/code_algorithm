height, wide = map(int, input().split())
A = [list(map(str, input().split())) for i in range(height)]
def draw_frame(h, w , a):
    print("#"*(w+2))
    for value in a:
        print("#" + value[0] +"#")
    print("#"*(w+2))

draw_frame(height, wide, A)

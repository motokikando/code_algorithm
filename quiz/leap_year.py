
input_line = int(input())
for i in range(input_line):
    N = int(input())
    if  N % 100 == 0 and N % 400 != 0:
        print(str(N) + " " +  "is not a leap year")

    else:
        if N % 4 == 0:
            print(str(N) + " " +  "is a leap year")
        else:
            print(str(N) + " " +  "is not a leap year")

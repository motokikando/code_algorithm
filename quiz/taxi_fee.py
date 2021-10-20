#taxi[0] 初乗り距離 a_i
#taxi[1] 初乗り運賃 b_i
#taxi[2] 加算距離 c_i
#taxi[3] 加算運賃 d_i
N, X = map(int, input().split())
def taxi_select(N: int, X: int) -> int:
  grid = []
  result = []
  for i in range(N):
    taxi = list(map(int, input().strip().split()))
    taxi_fee =  ((X - taxi[0])//taxi[2]+1)*taxi[3]+taxi[1]
    grid.append(taxi)
    if X >= taxi[0]:
      result.append(taxi_fee)
    else:
      result.append(taxi[1])
  return print(min(result), max(result))

taxi_select(N, X)







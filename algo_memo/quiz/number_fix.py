S = '00.0.43.7.73000'
#Python では、小数点を含まない入力に関しては int 関数 を用いて数値として正しい形式にできる
#.カンマがSに含まれていない時
if '.' not in S:
  #int()でSを出力
  print(int(S))
#それ以外
else:
  ans = '' #最終的な出力
  start = 0#start = 0とする
  #len(S)の範囲だけforループ
  for i in range(len(S)):
    if S[i] != '0':
      if S[i] == '.':
        ans += "0" #整数1の位の0を足
        start = i #小数点からスタートできるようにしておく
        break #ループを抜ける
  last = 0
  for i in range(len(S)):
    if S[i] != "0":
      last = i #小数の最後の値は0ではなく整数にするため
  first_dot = S.find(".")
  for i in range(start, last+1):
    if S[i] != '.':
      ans += S[i]
    elif i == first_dot:
      ans += S[i]
  print(ans)
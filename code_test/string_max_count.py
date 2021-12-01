from collections import Counter
from typing import Tuple

def string_max_count(s: str) -> None:

    count = {}
    for i in s:
        if i in count:
            #count[]で値を取得し，lower()で小文字に変換する
            #要素をcount[]で数え+1する
            count[i.lower()] = count[i.lower()]+1
        else:
            count[i.lower()] = 1
    #スペースを除外
    count.pop(' ')
    #ソート
    count2 = sorted(count.items(),key=lambda x:x[1], reverse=True)
    print(count2[0])



if __name__ == '__main__':
    s = 'This is a pen. This is an apple. Applepen'
    string_max_count(s)





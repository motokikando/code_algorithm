# input X:[1,2,3,4,4,5,5,8,10]
#     Y:[4,5,5,5,6,7,8,8,10]
from collections import Counter
from typing import List

def list_judge(x:List,y:List) -> None:
    counter_x = Counter(x)
    counter_y = Counter(y)
    # print(counter_x)
    # print(counter_y)
    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x) #yのvalueを取得

        if value_y:
            if value_y > value_x:
                x = [i for i in x if i != key_x]
                # print(x)
            elif value_y < value_x:
                y = [i for i in y if i != key_x]
                # print(y)




if __name__ == '__main__':
    x = [1,2,3,4,4,5,5,8,10]
    y = [4,5,5,5,6,7,8,8,10]
    print('x = ', x)
    print('y = ', y)
    list_judge(x, y)
    print('x = ', x)
    print('y = ', y)

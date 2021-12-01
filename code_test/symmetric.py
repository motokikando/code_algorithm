
input = [(1,2),(3,5),(4,7),(5,3),(7,4)]
output = [(5,3), (7,4)]
l = []

from typing import List, Iterator, Tuple

def find_pair(pairs:List[Tuple[int,int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield pair

if __name__ == '__main__':
    l =  [(1,2),(3,5),(4,7),(5,3),(7,4)]
    for r in find_pair(l):
        print(r)




# from typing import List, Iterator, Tuple

# def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int,int]]:
#     cache = {}
#     for pair in pairs:
#         first, second = pair[0], pair[1]
#         value = cache.get(second)
#         if not value:
#             #辞書型として定義
#             cache[first] = second
#         elif value == first:
#             yield pair



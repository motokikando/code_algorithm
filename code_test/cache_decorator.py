from functools import lru_cache
import time


def memoize(f):
    cache = {} #メモリとしてキャッシュの辞書を定義
    def _wrapper(n):
        #cacheがない場合そのままkeyをn valueをf(n)として値を格納
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return _wrapper

@memoize
def long_func(num:int) -> int:
    r = 0
    for i in range(1000000):
        r += num*i
    return r

if __name__ == '__main__':
    for i in range(10):
        print(long_func(i))
    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)



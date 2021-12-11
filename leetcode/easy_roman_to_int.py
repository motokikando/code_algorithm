
def romanToInt(s:str) -> int:
    roman_1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_2 = {'IV':4,'IX':9,'XL':40, 'XC':90, 'XD':400, 'CM':900}

    ans = 0
    for k, v in roman_2.items():
        if k in s:
            ans += roman_2[k]
            s = s.replace(k, '')

    for i in range(len(s)):
        if s[i] in roman_1:
            ans += roman_1[s[i]]

    return ans


if __name__ == '__main__':
    s = input()
    print(romanToInt(s))



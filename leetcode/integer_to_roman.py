class Solution:
    def intToRoman(self, num:int) -> str:
        ans = []

        #1000の位
        q, mod = divmod(num, 1000)
        ans.append('M'*q)

        #100の位
        q, mod = divmod(mod, 100)
        if q == 9:
            ans.append('CM')
        elif 5 <= q < 9:
            ans.append('D'+'C'*(q-5))
        elif q == 4:
            ans.append('CD')
        else:
            ans.append('C'*q)

        #10の位
        q, mod = divmod(mod, 10)
        if q == 9:
            ans.append('XC')
        elif 5 <= q < 9:
            ans.append('L'+'X'*(q-5))
        elif q == 4:
            ans.append('XL')
        else:
            ans.append('X'*q)

        #1の位
        if mod == 9:
            ans.append('IX')
        elif 5 <= mod < 9:
            ans.append('V'+'I'*(mod-5))
        elif mod == 4:
            ans.append('IV')
        else:
            ans.append('I'*mod)

        return ''.join(ans)











if __name__ == '__main__':
    num = 58
    s = Solution()
    print(s.intToRoman(num))

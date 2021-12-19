class Solution2:
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



class Solution:
    def intToRoman(self, num:int) -> str:
        roman_1 = ['I', 'X', 'C', 'M']
        roman_5 = ['V', 'L', 'D']
        ans = []

        for i in range(len(str(num))):
            n = num % 10
            if n == 9:
                ans.append(roman_1[i]+roman_1[i+1])
            elif 5 <= n < 9:
                ans.append(roman_5[i]+roman_1[i]*(n-5))
            elif n == 4:
                ans.append(roman_1[i] + roman_5[i])
            elif 1<= n < 4:
                ans.append(roman_1[i]*n)
            num //= 10
        return ''.join(reversed(ans))






if __name__ == '__main__':
    num = 3
    s = Solution()
    print(s.intToRoman(num))

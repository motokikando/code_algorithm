class Solution:
    def intToRoman(self, num:int) -> str:
        roman_1 = ['I', 'X', 'C', 'M']
        roman_5 = ['V', 'L', 'D']
        ans = []

        for i in range(num):
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
    num = 13
    s = Solution()
    print(s.intToRoman(num))

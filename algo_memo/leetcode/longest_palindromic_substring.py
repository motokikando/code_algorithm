class Solution:
    def longestPalindrome(self, s:str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s
        count = 0
        ans = ''
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                s_part = s[i:j]
                if s_part == s_part[::-1] and len(s_part) > count:
                    ans = s_part
                    count = len(s_part)
        return ans


if __name__== '__main__':
    a = Solution()
    string = 'bgjgikuoukskjgsk'
    print(a.longestPalindrome(string))


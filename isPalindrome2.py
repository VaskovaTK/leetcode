class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        newS = str()
        for i in range(len(s)):
            ordS = ord(s[i])
            if ordS>=97 and ordS<= 122 or ordS>=48 and ordS<=57:
                newS+=s[i]
        first = 0
        last = len(newS)-1
        while first<last:
            if newS[first] == newS[last]:
                first+=1
                last-=1
            else:
                # print(False)
                return False
        # print(True)
        return True
sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")
sol.isPalindrome("race a car")


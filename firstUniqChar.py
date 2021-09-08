class Solution:
    def firstUniqChar(self, s: str) -> int:
        lettersArr = [0]*27
        remLetter = list()
        for i in range(len(s)):
            lettersArr[ord(s[i]) - 96]+=1
        for l in range(len(lettersArr)):
            if lettersArr[l] == 1:
                remLetter.append(chr(l+96))
        for i in range(len(s)):
            if s[i] in remLetter:
                return i
        return -1


sol = Solution()
sol.firstUniqChar("llloveyouz")
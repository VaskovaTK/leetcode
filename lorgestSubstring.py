class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ret = self.recursion(s, k,0, len(s))
        return ret
    def recursion (self, subStr: str, k: int, startIndex: int, finishIndex: int):
        if len(subStr)<k:
            return 0
        letters = [0]*27
        for i in range (startIndex, finishIndex):
            numberFromLetter = (ord(subStr[i])-96)
            if letters[numberFromLetter] ==0:
                letters[numberFromLetter] = 1
            else:
                letters[numberFromLetter]+=1
        maxLen = 0
        for index in range(startIndex, finishIndex):
            numberFromLetter = (ord(subStr[index])-96)
            if letters[numberFromLetter] < k:
                newStartIndex = finishIndex
                for secondStartIndex in range(index+1, finishIndex):
                    numberForStartIndex = (ord(subStr[secondStartIndex])-96)
                    if letters[numberForStartIndex]>=k:
                        newStartIndex = secondStartIndex
                        break
                len1 = self.recursion(subStr,k, startIndex, index)
                len2 = self.recursion(subStr,k, newStartIndex, finishIndex)
                maxLen = max(maxLen, len1, len2)
                return maxLen
        return finishIndex-startIndex


sol = Solution()
print(sol.longestSubstring(s = "ababbc", k = 2)) #5
print(sol.longestSubstring("aaabbb",3)) #6
print(sol.longestSubstring('aaabb', 3)) #3
print(sol.longestSubstring('aabbbpqrst', 3)) #3
print(sol.longestSubstring("ababacb",3)) # 0
print(sol.longestSubstring("aaaaaaaaaaaabcdefghijklmnopqrstuvwzyz",3))
print(sol.longestSubstring("bbaaacbd",3)) #3

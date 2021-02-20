class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ret = self.recursion(s, k,0, len(s))
        return ret
    def recursion (self, subStr: str, k: int, startIndex: int, finishIndex: int):
        if len(subStr)<k:
            return 0
        letters = {}
        for i in range (startIndex, finishIndex):
            if subStr[i] not in letters:
                letters[subStr[i]] = 1
            else:
                letters[subStr[i]]+=1
        maxLen = 0
        for index in range(startIndex, finishIndex):
            if letters[subStr[index]] < k:
                newStartIndex = finishIndex
                for secondStartIndex in range(index+1, finishIndex):
                    if letters[subStr[secondStartIndex]]>=k:
                        newStartIndex = secondStartIndex
                        break
                len1 = self.recursion(subStr,k, startIndex, index)
                len2 = self.recursion(subStr,k, newStartIndex, finishIndex)
                maxLen = max(maxLen, len1, len2)
                return maxLen
        return finishIndex-startIndex


sol = Solution()
# print(sol.longestSubstring(s = "ababbc", k = 2)) #5
# print(sol.longestSubstring("aaabbb",3)) #6
# print(sol.longestSubstring('aaabb', 3)) #3
# print(sol.longestSubstring('aabbbpqrst', 3)) #3
# print(sol.longestSubstring("ababacb",3)) # 0
# print(sol.longestSubstring("aaaaaaaaaaaabcdefghijklmnopqrstuvwzyz",3))
print(sol.longestSubstring("bbaaacbd",3)) #3

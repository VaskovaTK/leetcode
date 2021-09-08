class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for i in range(len(s)):
            if s[i] not in sDict.keys():
                sDict[s[i]] = 1
            else:
                sDict[s[i]] +=1
        for i in range(len(t)):
            if t[i] not in tDict.keys():
                tDict[t[i]] = 1
            else:
                tDict[t[i]] +=1
        if sDict == tDict:
            return True
        else:
            return False



# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sArray = [0]*27
#         tArray =[0]*27
#         for i in range(0,len(s)):
#             indexInArray = ord(s[i])-96
#             sArray[indexInArray] +=1
#         for i in range(0,len(t)):
#             indexInArray = ord(t[i])-96
#             tArray[indexInArray] +=1
#         for j in range (0,len(sArray)):
#             if tArray[j] != sArray[j]:
#                 return False
#         return True

sol = Solution()
# sol.isAnagram('abc','bca')
sol.isAnagram(s = "anagram", t = "nagaram")
# sol.isAnagram(s = "rat", t = "car")
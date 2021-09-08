class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if strs[0]:
            example = strs[0]
        else:
            return ""
        common = ""
        lenght = len(strs)
        flag = False
        for e in range (0, len(example)):
            if flag == True:
                break
            for i in range (0, lenght):
                if e <= len(strs[i])-1:
                    if strs[i][e] == example[e]:
                        if i == lenght-1:
                            common+=example[e]
                        else:
                            continue
                    else:
                        flag = True
                        break
                else:
                    flag = True
                    break
        # print(common)
        return common
sol = Solution()
sol.longestCommonPrefix(["flower","flow","flight"])
sol.longestCommonPrefix(["dog","racecar","car"])
sol.longestCommonPrefix(["ab", "a"])

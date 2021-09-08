class Solution:
    def romanToInt(self, s: str) -> int:
        # lettersDict = {}
        # lettersDict["I"] = 1
        # lettersDict["V"] = 5
        # lettersDict["X"] = 10
        # lettersDict["L"] = 50
        # lettersDict["C"] = 100
        # lettersDict["D"] = 500
        # lettersDict["M"] = 1000
        retNumber = 0
        lenght = len(s)
        for i in range(0,lenght):
            if s[i] == "I":
                if i+1<=lenght-1 and s[i+1]=="V":
                    retNumber+=4
                elif i+1<=lenght-1 and s[i+1] =="X":
                    retNumber+=9
                else:
                    retNumber+=1
            elif s[i] == "V":
                if i-1>=0 and s[i-1] =="I":
                    continue
                else:
                    retNumber+=5
            elif s[i] == "X":
                if i-1>=0 and s[i-1] == "I":
                    continue
                elif i+1<=lenght-1 and s[i+1] == "L":
                    retNumber+=40
                elif i+1<=lenght-1 and s[i+1] == "C":
                    retNumber +=90
                else:
                    retNumber+=10
            elif s[i] == "L":
                if i-1>=0 and s[i-1] == "X":
                    continue
                else:
                    retNumber+=50
            elif s[i] == "C":
                if i-1>=0 and s[i-1] == "X":
                    continue
                elif i+1<=lenght-1 and s[i+1] == "D":
                    retNumber+=400
                elif i+1<=lenght-1 and s[i+1] == "M":
                    retNumber +=900
                else:
                    retNumber+=100
            elif s[i] == "D":
                if i-1>=0 and s[i-1] == "C":
                    continue
                else:
                    retNumber+=500
            elif s[i] == "M":
                if i-1>=0 and s[i-1] == "C":
                    continue
                else:
                    retNumber+=1000
        # print(retNumber)
        return retNumber

sol = Solution()
# sol.romanToInt("IV")
# sol.romanToInt("MCMXCIV")
# sol.romanToInt("LVIII")
# sol.romanToInt("MMMCDXC")
sol.romanToInt("LXXIX")



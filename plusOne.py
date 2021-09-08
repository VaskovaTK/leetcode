class Solution:
    def plusOne(self, digits: list) -> list:
        flag = False
        if digits[-1]<9:
            digits[-1] +=1
        else:
            for i in range(-1,-len(digits)-1,-1):
                if digits[i]<9:
                    digits[i] +=1
                    flag = True
                    break
                else:
                    digits[i] = 0
            if flag == False:
                digits.insert(0,1)
        # print(digits)
        return digits

sol = Solution()
sol.plusOne([9,9])
sol.plusOne([0])

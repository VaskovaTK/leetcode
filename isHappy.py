class Solution:
    def isHappy(self, n: int) -> bool:
        wasN =[]
        count = 0
        while True:
            if n >=10:
                count +=(n%10)**2
                n = n//10
            else:
                count+=(n)**2
                if count == 1:
                    # print(True)
                    return True
                if count in wasN:
                    # print(False)
                    return False
                wasN.append(count)
                n = count
                count = 0
sol = Solution()
sol.isHappy(123)
sol.isHappy(19)
sol.isHappy(2)
sol.isHappy(7)

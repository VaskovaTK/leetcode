class Solution:
    def reverse(self, x: int) -> int:
        numberList = ""
        if x < -2**31 or x >2**31 - 1:
            return 0
        if x == 0:
            return 0
        if x<0:
            numberList+="-"
            x = x*(-1)
        while x !=0:
            if x//10 !=0:
                newNum= x%10
                x = x//10
                numberList+=str(newNum)
            if x <10:
                numberList+=str(x)
                x = 0
        ret = int(numberList)
        if ret < -2**31 or ret >2**31 - 1:
            return 0
        else:
            return ret


sol = Solution()
sol.reverse(123)
sol.reverse(-215)
sol.reverse(0)
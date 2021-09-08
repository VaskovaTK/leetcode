class Solution:
    def countPrimes(self, n: int) -> int:
        # import math
        # count = 0
        # for i in range(2, n):  # O(n)
        #     factors = 0
        #     for j in range(2, math.floor(math.sqrt(i)) + 1):  # O(sqrt(n))
        #         if i % j == 0:
        #             factors += 1
        #     if factors == 0:
        #         count += 1
        # return count
        if n<=2:
            return 0
        n-=1
        import math
        count = 0
        while n>1:
            if n%2 ==0:
                n-=1
                continue
            flag = False
            prime = 0
            square = round(math.sqrt(n))+1
            for i in range(1,square):
                if n%i ==0:
                    prime+=1
                    if prime>=2:
                        flag = True
                        break
            if flag != True:
                count+=1
            n-=1
        print(count+1)
        return count+1



        # count = 0
        # savedN = n
        # primes = list()
        # n =1
        # while n<savedN:
        #     prime = 0
        #     if (n % 1) == 0:
        #         prime+=1
        #     if (n % 2) == 0:
        #         prime+=1
        #     if (n % 3) == 0:
        #         prime+=1
        #     if (n % 4) == 0:
        #         prime+=1
        #     if (n % 5) == 0:
        #         prime+=1
        #     if (n % 6) == 0:
        #         prime+=1
        #     if (n % 7) == 0:
        #         prime+=1
        #     if (n % 8) == 0:
        #         prime+=1
        #     if (n % 9) == 0:
        #         prime+=1
        #     if n>9:
        #         if (n % n) == 0:
        #             prime += 1
        #         if prime ==2:
        #             for p in range(0,len(primes)):
        #                 if (n % primes[p]) == 0:
        #                     prime += 1
        #     if prime==2:
        #         count+=1
        #         primes.append(n)
        #     n +=1
        # # print(count)
        # return count

sol = Solution()
sol.countPrimes(3)
sol.countPrimes(10)
sol.countPrimes(10000)
sol.countPrimes(499979)
sol.countPrimes(499979)
# по времени не прошло

